import streamlit as st
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import os

# Set up Streamlit configuration
st.set_page_config(page_title="YouTube Video Downloader", page_icon=":arrow_down:", layout="centered")

# App title and description
st.title("YouTube Video Downloader 🔍⬇️")
st.markdown("Paste the YouTube URL below and click 'Download' to get your video!")

# Input URL
video_url = st.text_input("Enter YouTube video URL")

# Download button with logic
if st.button("Download⬇️"):
    if not video_url:
        st.warning("Please enter a URL.")
    else:
        with st.spinner("Processing..."):
            try:
                yt = YouTube(video_url)
                stream = yt.streams.get_highest_resolution()
                
                # Create a downloads directory if it doesn't exist
                if not os.path.exists("downloads"):
                    os.makedirs("downloads")
                
                # Define the download path
                download_path = stream.download(output_path="downloads")
                
                st.success("Video successfully downloaded!")
                st.balloons()
                
                # Read the downloaded file to enable download button
                with open(download_path, "rb") as file:
                    st.download_button(
                        label="Download Video",
                        data=file,
                        file_name=os.path.basename(download_path),
                        mime="video/mp4"
                    )

            except RegexMatchError:
                st.error("Invalid YouTube URL. Please try again.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Closing remark
st.markdown("Enjoy your videos!")
