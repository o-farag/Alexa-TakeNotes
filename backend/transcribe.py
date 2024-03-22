import os
import time
import boto3

def upload_file_to_s3(bucket_name, file_path, s3_client):
    key = file_path.split("/")[-1]  # Use the file name as the key in S3
    s3_client.upload_file(file_path, bucket_name, key)
    return f"s3://{bucket_name}/{key}"

def transcribe_audio(file_uri, transcribe_client):
    job_name = "patrick_test" + str(int(time.time()))  # Create a unique job name
    job_uri = file_uri
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',  # Change this to match your file format
        LanguageCode='en-US',  # Change this to match the language of your audio
        #OutputBucketName='h12324output'  # Change this to your bucket name
    )
    print(f"Transcription job {job_name} submitted.")
    return job_name

def transcribe_video(file_uri, transcribe_client):
    job_name = "patrick_test" + str(int(time.time()))  # Create a unique job name
    job_uri = file_uri
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp4',  # Change this to match your file format
        LanguageCode='en-US',  # Change this to match the language of your audio
        #OutputBucketName='h12324output'  # Could use custom bucket instead of default if desired
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
    else:
        print("Transcription job is not yet complete.")

def main():
    bucket_name = "h12324bucket"
    file_path = "/home/sulehria/Downloads/confusion_sample.mp3" # Make this more modular
    s3_client = boto3.client('s3')
    file_uri = upload_file_to_s3(bucket_name, file_path, s3_client)
    transcribe_client = boto3.client('transcribe')
    job_name = transcribe_audio(file_uri, transcribe_client)

    # Technically unneccessary, but useful for demonstration/seeing progress
    count = 0; inc = 5
    status = get_transcription_job_status(job_name, transcribe_client)
    while status != 'COMPLETED':
        time.sleep(inc) # Sleep for 3 seconds
        count += inc
        print(count, "Seconds elapsed.")
        status = get_transcription_job_status(job_name, transcribe_client)
    if status == 'COMPLETED':
        get_transcription_results(job_name, transcribe_client)

if __name__ == "__main__":
    main()
