from pydub import AudioSegment
import os

def convert_wav_to_midi(wav_file):
    # Waveファイルを読み込み
    audio = AudioSegment.from_wav(wav_file)

    # MIDIファイルに変換
    midi_file = os.path.splitext(wav_file)[0] + ".midi"
    audio.export(midi_file, format="midi")

    print(f"Conversion successful. MIDIファイル: {midi_file}")

if __name__ == "__main__":
    # 同じフォルダにあるWaveファイルの名前（拡張子を含む）を指定
    wave_filename = "company_song.wav"

    # WaveファイルをMIDIに変換
    convert_wav_to_midi(wave_filename)
