import os
import time
import boto3

def upload_file_to_s3(bucket_name, file_path, s3_client):
    key = file_path.split("/")[-1]  # Use the file name as the key in S3
    s3_client.upload_file(file_path, bucket_name, key)
    return f"s3://{bucket_name}/{key}"

def transcribe_audio(file_uri, transcribe_client):
    job_name = "transcription_test" + str(int(time.time()))  # Create a unique job name
    job_uri = file_uri
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',  # Change this to match your file format
        LanguageCode='en-US',  # Change this to match the language of your audio
        Settings={
            'ShowSpeakerLabels': True,
            'MaxSpeakerLabels': 2
        }
    )
    print(f"Transcription job {job_name} submitted.")
    return job_name

def get_transcription_job_status(job_name, transcribe_client):
    response = transcribe_client.get_transcription_job(
        TranscriptionJobName=job_name
    )
    status = response['TranscriptionJob']['TranscriptionJobStatus']
    return status

def get_transcription_results(job_name, transcribe_client):
    response = transcribe_client.get_transcription_job(
        TranscriptionJobName=job_name
    )
    if response['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        transcription_url = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
        print(f"Transcription results available at: {transcription_url}")
        file_name = f"{job_name}.txt"
        # Download the transcription file
        os.system(f"wget -O {file_name} {transcription_url}")
        print(f"Transcription result downloaded as {file_name}")
    else:
        print("Transcription job is not yet complete.")

def download_transcription_result(job_name, transcribe_client):
    response = transcribe_client.get_transcription_job(
        TranscriptionJobName=job_name
    )
    if response['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        transcription_uri = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
        file_name = f"{job_name}.txt"
        # Download the transcription file
        os.system(f"wget -O {file_name} {transcription_uri}")
        print(f"Transcription result downloaded as {file_name}")
    else:
        print("Transcription job is not yet complete.")

def main():
    bucket_name = "h12324bucket"
    file_path = "/home/sulehria/Code/AWS_Hacks_2024/Learn_Functions.mp3"  # Update this with the path to your local file
    s3_client = boto3.client('s3')
    file_uri = upload_file_to_s3(bucket_name, file_path, s3_client)
    #file_uri = "s3://your-bucket-name/your-file-path"  # Update this with your file location
    transcribe_client = boto3.client('transcribe')
    job_name = transcribe_audio(file_uri, transcribe_client)

    # Add this to main() after transcribe_audio() function call
    count = 0
    status = get_transcription_job_status(job_name, transcribe_client)
    while status != 'COMPLETED':
        time.sleep(3) # Sleep for 3 seconds
        count += 3
        print(count, "Seconds elapsed.")
        status = get_transcription_job_status(job_name, transcribe_client)
    if status == 'COMPLETED':
        get_transcription_results(job_name, transcribe_client)

if __name__ == "__main__":
    main()
