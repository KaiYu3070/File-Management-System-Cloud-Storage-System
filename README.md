# File Management System (Cloud Storage) with YouTube Video Download Support

This is a cloud-based file management system that allows users to upload, download, and organize files, including YouTube videos. The system enables users to manage their files efficiently, create custom folders, and even download videos from YouTube directly to their cloud storage. 

## Features

- **File Upload**: Upload files from your local machine to the cloud storage.
- **File Download**: Download any file stored in the system.
- **Folder Management**: Organize your files into folders for easy management.
- **YouTube Video Download**: Download videos from YouTube in various formats (MP4, WebM, etc.) and resolutions (from 144p to 4K).
- **Custom Folders**: You can specify the folder in which you want to store the downloaded video.
- **No Database**: The system does not rely on a traditional database but uses a custom file system format to store file metadata.

## Installation

To install and run the File Management System locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/File-Management-System-Cloud-Storage-System.git
   ```

2. Navigate to the project directory:
   ```bash
   cd File-Management-System-Cloud-Storage-System
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python manage.py runserver
   ```

## Usage

Once the server is running, open your browser and go to:

```
http://127.0.0.1:8000
```

You can now access the file management interface. Here are some of the main features:

### File Upload
- Navigate to the "Upload" section of the app.
- Select a file from your local machine and click "Upload" to store it in your cloud storage.

### File Download
- Browse your cloud storage and select the file you want to download.
- Click the "Download" button to retrieve the file to your local machine.

### Folder Management
- Create folders by clicking the "Create Folder" button in the app.
- Organize your files by dragging and dropping them into these folders.

### YouTube Video Download
- In the "YouTube Video Download" section, enter the URL of the YouTube video you want to download.
- Select the folder in which you'd like to store the video.
- Choose the video format (MP4, WebM) and quality (144p to 4K).
- Click "Download" to download the video to the selected folder.

**Note**: The video will be downloaded directly to your cloud storage and will be saved in the folder of your choice.

## Supported Video Formats and Resolutions

This system supports downloading videos in **MP4** and **WebM** formats from YouTube, with the following resolution options:

- **144p**
- **240p**
- **360p**
- **480p**
- **720p**
- **1080p**
- **1440p (2K)**
- **2160p (4K)**

You can select the video format and resolution before downloading. By default, **MP4** is preferred, but **WebM** can also be chosen if available.

### Example Download Formats

- **MP4 (144p)**: Low quality video for small file size and faster download speed.
- **MP4 (720p)**: Standard HD quality video.
- **MP4 (1080p)**: Full HD quality video.
- **MP4 (1440p / 2K)**: Higher definition for those who need a sharper image.
- **MP4 (2160p / 4K)**: Best quality for ultra-high definition video.
- **WebM (Any Resolution)**: A modern video format for web usage, supported by most browsers and devices.

## Screenshots

Here are some screenshots of the system in action:

![Dashboard Screenshot](/pic/1.png)
*Dashboard showing file and folder management interface.*

![File Upload Screenshot](/pic/2.png)
*File upload interface showing selected file for upload.*

![YouTube Video Download Screenshot](/pic/3.png)
![YouTube Video Download Screenshot](/pic/4.png)
*YouTube video download interface showing URL input and folder selection.*

## Technologies Used

- **Django**: Web framework for building the backend of the system.
- **yt-dlp**: A command-line tool for downloading videos from YouTube and other platforms.
- **SQLite**: Database used for storing file metadata and user information.
- **HTML/CSS**: Frontend design and layout for the user interface.
- **JavaScript**: Used for dynamic interactions and AJAX requests.

## Video Download from YouTube

To download videos from YouTube, the system uses `yt-dlp`, a popular open-source tool for downloading videos from various websites, including YouTube. The video download functionality supports various formats and qualities (e.g., 144p, 720p, 1080p, etc.). You can select your desired video format and resolution before downloading.

### Supported Formats

- **MP4**: Widely supported format for videos.
- **WebM**: A modern video format supported by most browsers.

The download process also handles folder management, allowing you to store downloaded videos in specific folders within your cloud storage.

## Example Workflow

1. Open the app and log in (if necessary).
2. Go to the "YouTube Video Download" section.
3. Enter a YouTube URL and select the desired video quality and format (e.g., `720p` and `MP4`).
4. Choose a folder to store the downloaded video.
5. Click "Download" to start downloading the video to your cloud storage.
6. Organize downloaded videos as needed by creating folders and moving files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. We welcome contributions such as bug fixes, new features, or improvements.

## Contact

If you have any questions or feedback, feel free to reach out to me at [lapjhon4@gmail.com].
```

### Key Updates:
1. **Supported Formats and Resolutions**:
   - Added detailed information about supported video formats (MP4 and WebM) and resolutions (144p to 4K).
2. **Video Download Workflow**:
   - Clarified how users can choose video quality (resolution and format) before downloading.
3. **Screenshots**:
   - Placeholder for screenshots showing the dashboard, file upload, and YouTube video download interface.
4. **Technologies Used**:
   - Included `yt-dlp` for downloading videos from YouTube, which supports various formats and resolutions.

### Action:
- Replace `path_to_your_screenshot_1.png`, `path_to_your_screenshot_2.png`, and `path_to_your_screenshot_3.png` with the actual file paths to your screenshots.