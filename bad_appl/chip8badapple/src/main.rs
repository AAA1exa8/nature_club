use colored::*;
use ffmpeg_next::format::{input, Pixel};
use ffmpeg_next::media::Type;
use ffmpeg_next::software::scaling::flag::Flags;
use ffmpeg_next::util::frame::video::Video;
use std::env;
use std::io::{Read, Write};

const WIDTH: u8 = 64;
const HEIGHT: u8 = 32;

fn main() -> Result<(), ffmpeg_next::Error> {
    ffmpeg_next::init().unwrap();
    if (WIDTH as u32) * (HEIGHT as u32) % 64 != 0 {
        panic!("Width * Height must be a multiple of 64.");
    }

    if let Ok(mut ictx) = input(&env::args().nth(1).expect("Cannot open file.")) {
        let input = ictx
            .streams()
            .best(Type::Video)
            .ok_or(ffmpeg_next::Error::StreamNotFound)?;
        let video_stream_index = input.index();

        let context_decoder =
            ffmpeg_next::codec::context::Context::from_parameters(input.parameters())?;
        let mut decoder = context_decoder.decoder().video()?;

        // clion doesn't like use for this...
        let mut scaler = ffmpeg_next::software::scaling::context::Context::get(
            // input
            decoder.format(),
            decoder.width(),
            decoder.height(),
            // output
            Pixel::GRAY8,
            WIDTH as u32,
            HEIGHT as u32,
            Flags::BICUBIC,
        )?;

        let mut frame_index = 0;

        let mut full_data = Vec::new();
        let mut receive_and_process_decoded_frames =
            |decoder: &mut ffmpeg_next::decoder::Video| -> Result<(), ffmpeg_next::Error> {
                let mut decoded = Video::empty();
                while decoder.receive_frame(&mut decoded).is_ok() {
                    let mut bw_frame = Video::empty();
                    scaler.run(&decoded, &mut bw_frame)?;
                    let data = bw_frame.data(0);

                    data.chunks(64)
                        .map(|s| s.iter().map(|i| *i < 128).collect::<Vec<_>>())
                        .for_each(|chunk| {
                            let mut chunk_b: u64 = 0;
                            chunk.iter().enumerate().for_each(|(i, &b)| {
                                if b {
                                    chunk_b |= 1 << i;
                                }
                            });
                            full_data.push(chunk_b);
                        });

                    frame_index += 1;
                }
                Ok(())
            };

        for (stream, packet) in ictx.packets() {
            if stream.index() == video_stream_index {
                decoder.send_packet(&packet)?;
                receive_and_process_decoded_frames(&mut decoder)?;
            }
        }
        decoder.send_eof()?;
        receive_and_process_decoded_frames(&mut decoder)?;
        // full_data
        //     .chunks((WIDTH as usize) * (HEIGHT as usize) / 64)
        //     .for_each(|chunk| {
        //         print_frame(chunk);
        //         std::io::stdout().flush().unwrap();
        //         std::thread::sleep(std::time::Duration::from_millis(16));
        //     });

        // write all to file
        let mut file = std::fs::File::create("output.bin").unwrap();
        for &chunk in full_data.iter() {
            file.write_all(&chunk.to_le_bytes()).unwrap();
        }
        let mut test_file = std::fs::File::open("output.bin").unwrap();
        let mut test_data = Vec::new();
        test_file.read_to_end(&mut test_data).unwrap();
        test_data
            .chunks(8)
            .map(|s| u64::from_le_bytes(s.try_into().unwrap()))
            .collect::<Vec<_>>()
            .chunks((WIDTH as usize) * (HEIGHT as usize) / 64)
            .for_each(|chunk| {
                print_frame(chunk);
                std::io::stdout().flush().unwrap();
                std::thread::sleep(std::time::Duration::from_millis(16));
            });
    }

    Ok(())
}

fn print_frame(data: &[u64]) {
    let mut frame = String::new();
    data.iter().for_each(|&chunk| {
        for i in 0..64 {
            if chunk & (1 << i) != 0 {
                frame.push_str("  ");
            } else {
                frame.push_str("██");
            }
        }
        frame.push('\n');
    });
    print!("{}", frame);
}
