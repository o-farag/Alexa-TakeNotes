import React, { useState } from 'react';
import { Text, FileButton, Button, Card, Image, Flex } from '@mantine/core';

type ImportCardProps = {
    label: string,
    imgSrc: string,
    setFile: (file: File | null) => void;
}

function ImportCards(props: ImportCardProps) {
    return (
        <Card padding="lg" radius="md" withBorder>
            <Flex h='18em' w='15em' direction='column' align='center' justify='center' gap='1em'>
                <Image
                    src={props.imgSrc}
                    h='100'
                    fit='contain'
                />
                <Text mt='1.5em' ta='center' fw={500}>{props.label}</Text>
                <FileButton onChange={props.setFile}>
                    {(props) => <Button  {...props} w='10em' mt='0.5em' radius="md" variant='outline'>
                        Import
                    </Button>}
                </FileButton>
            </Flex>
        </Card>
    );
}

export default ImportCards;
