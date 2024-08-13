import subprocess
import os

def cut_video_into_images(input_file, output_dir):
    """
    Cuts a video into images.

    Parameters:
    input_file (str): The path to the input video file.
    output_dir (str): The directory where the output images will be saved.

    Returns:
    None
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.splitext(os.path.basename(input_file))[0]

    # Run the ffmpeg command
    command = f"ffmpeg -i {input_file} -vf fps=1/5 {output_dir}/%04d_{filename}.png"
    subprocess.run(command, shell=True)
    

def capture_files(directory, filename):
    """
    Captures files from a specified directory that start with a given filename.

    Parameters:
        directory (str): The path to the directory to search for files.
        filename (str): The filename prefix to search for.

    Returns:
        list: A list of file paths that match the specified filename prefix.
    """
    captured_files = []
    for file in os.listdir(directory):
        if file.startswith(filename):
            captured_files.append(os.path.join(directory, file))
    return captured_files

# Example usage
directory = r"C:\Users\pcash\Desktop"
filename = "ABYSS"
captured_files = capture_files(directory, filename)
print(captured_files)

# Example usage
for file in captured_files:
    input_file = file
    print("file name: ", file)
    output_dir = str(os.path.split(input_file)[-1]).split(".")[0]
    cut_video_into_images(input_file, output_dir)
