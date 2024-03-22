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
            <Button w='7em'>Go!</Button>
        </Flex>
    );
}

export default Generate;
