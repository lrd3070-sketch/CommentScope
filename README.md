# CommentScope
An open-source Python tool for collecting public YouTube comments and converting the data to a csv file

It uses the YouTube Data API v3 to collect video comments and replies and export them to CSV files for further analysis.

## Features

- Collect top-level comments from YouTube videos.
- Retrieve replies associated with top-level comments.
- Extract useful data, including:
  - Comment and reply IDs
  - Comment text
  - Like counts
  - Publication timestamps
- Export collected data to CSV format.

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/CommentScope.git
cd CommentScope
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

## Configuration

CommentScope requires a YouTube Data API v3 key.

1. Visit [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a Google Cloud project.
3. Enable YouTube Data API v3.
4. Generate an API key.
5. Create a `.env` file in the project directory.

Add the following line:

```env
YOUTUBE_API_KEY=your_api_key_here
```

Never commit your `.env` file or actual API key to GitHub.

## Usage

Run the application:

```bash
python main.py
```

Provide the YouTube video URL when prompted.

The collected comment data will be exported as a CSV file.

## Data Collection

CommentScope collects available comment information through the official YouTube Data API.

The collected data may include:

| Field | Description |
|---|---|
| comment_id | Unique comment identifier |
| reply_id | Unique reply identifier |
| text | Comment or reply content |
| likes | Number of likes |
| published_at | Publication timestamp |

The exact CSV structure depends on how comments and replies are organized during export.

## Limitations

- Requires a valid YouTube Data API key.
- Subject to YouTube API quotas and restrictions.
- Private, deleted, disabled, or otherwise inaccessible comments cannot be collected.
- The number of collected comments may differ from the count displayed on YouTube.

## Project Status

CommentScope is under active development.

Current focus:
- YouTube comment and reply collection
- Reliable pagination
- CSV data export

Potential future improvements:
- Improved data organization
- Comment filtering and search
- Sentiment analysis
- AI-assisted qualitative analysis

Supported formats include:

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`

Enter the maximum number of comments to collect.

### 4. Export results

CommentScope saves the collected top-level comments to `youtube_comments.csv`.

The exported dataset includes comment IDs, text, likes, and publication dates.

**Note:** This version collects public top-level comments only. Replies and AI-powered analysis are planned for future releases.