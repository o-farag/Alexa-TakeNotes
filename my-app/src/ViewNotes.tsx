import React, { useState } from 'react';
import { Text, Flex, Divider } from '@mantine/core';
import { IconNote } from '@tabler/icons-react';
import FileExplorer from './components/fileExplorer';

function ViewNotes() {
    return (
        <Flex direction='column' w='100%'>
            <Flex direction='row' align='center' ml='1em' mt='0.5em'>
                <IconNote></IconNote>
                <Text fz='lg' fw='500' p='0.5em'>Notes</Text>
            </Flex>
            <Divider></Divider>
            <FileExplorer bucketName={'notes-drive'}></FileExplorer>
        </Flex>
    );
}

export default ViewNotes;
