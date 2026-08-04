import sys
from pymediainfo import MediaInfo

def extract_metadata(file_path: str) -> None:
    media_info = MediaInfo.parse(file_path)
    if not media_info.tracks:
        print(f"No tracks found in '{file_path}'.")
        return
    for track in media_info.tracks:
        if track.track_type == 'General':
            print(f"Format: {track.format}")
            print(f"File Size: {track.file_size} bytes")
            print(f"Duration: {track.duration} ms")
            print(f"Overall Bit Rate: {track.overall_bit_rate} bps")
        elif track.track_type == 'Video':
            print("\nVideo Track:")
            print(f"Format: {track.format}")
            print(f"Codec: {track.codec}")
            print(f"Width: {track.width} pixels")
            print(f"Height: {track.height} pixels")
            print(f"Frame Rate: {track.frame_rate} fps")
        elif track.track_type == 'Audio':
            print("\nAudio Track:")
            print(f"Format: {track.format}")
            print(f"Codec: {track.codec}")
            print(f"Channels: {track.channel_s}")
            print(f"Sample Rate: {track.sample_rate} Hz")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path-to-video>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        extract_metadata(file_path)
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Error: could not read metadata: {exc}", file=sys.stderr)
        sys.exit(1)

