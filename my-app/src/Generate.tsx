import React, { useState } from 'react';
import { Text, Button, Flex, Image } from '@mantine/core';
import ImportCards from './components/importCards';
import audio_rec from './resources/audio_rec.png';
import slides from './resources/slides.png';
import notes from './resources/notes.png';
import alexa from './resources/alexa_icon.png';
function Generate() {
    const [recordingFile, setRecordingFile] = useState<File | null>(null);
    const [slidesFile, setSlidesFile] = useState<File | null>(null);
    const [textFile, setTextFile] = useState<File | null>(null);

    const generate = async () => {
        const files = {
            recording: recordingFile ? recordingFile.name : undefined,
            slides: slidesFile ? slidesFile.name : undefined,
            text: textFile ? textFile.name : undefined,
        };

        // Filter out undefined properties if you don't want them in the final JSON
        const filteredFiles = Object.entries(files).reduce((acc, [key, value]) => {
            if (value !== undefined) acc[key] = value;
            return acc;
        }, {} as { [key: string]: string });

        // Convert the object to a JSON string
        const filesJson = JSON.stringify(filteredFiles);

        try {
            const response = await fetch('http://127.0.0.1:5000/api/go', {
                method: 'POST',
                body: filesJson,
                headers: {
                    'Content-Type': 'application/json'
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            console.log('Files uploaded successfully!');
        } catch (error) {
            console.error('Error uploading files:', error);
        }
    };

    return (
        <Flex direction='column' justify='center' align='center' w='100%' gap='2em' mt='4em'>
            <Flex gap='2em'>
                <Image src={alexa} h='100' fit='contain'></Image>
                <Text fz='xl' fw='500'>Alexa, Take Notes...</Text>
            </Flex>
            <Flex gap='1em' mt='1.5em'>
                <ImportCards label={'Audio Recording'} imgSrc={audio_rec} setFile={setRecordingFile}></ImportCards>
                <ImportCards label={'Lecture Slides'} imgSrc={slides} setFile={setSlidesFile}></ImportCards>
                <ImportCards label={'Text Notes'} imgSrc={notes} setFile={setTextFile}></ImportCards>
            </Flex>
            <Button w='7em' onClick={generate}>Go!</Button>
        </Flex>
    );
}

export default Generate;
