import React from 'react';
import { IconNotes, IconPencilCog } from '@tabler/icons-react';
import { Box, NavLink } from '@mantine/core';
import { MantineProvider, createTheme, Flex } from '@mantine/core';
import Generate from './Generate';
import ViewNotes from './ViewNotes';
const data = [
  { icon: IconPencilCog, label: 'Take Notes', description: 'Generate notes' },
  { icon: IconNotes, label: 'Note Repository' },
];

function App() {
  const [active, setActive] = React.useState(0);

  const items = data.map((item, index) => (
    <NavLink
      href="#required-for-focus"
      key={item.label}
      active={index === active}
      label={item.label}
      description={item.description}
      leftSection={<item.icon size="1rem" stroke={1.5} />}
      onClick={() => setActive(index)}
    />
  ));

  return (
    <React.StrictMode>
      <MantineProvider theme={theme}>
        <Flex>
          <Flex h='100vh' bg='#F5F8FC' direction='column' w={220}>
            <Box w={220}>{items}</Box>
          </Flex>
          {active===0 ? 
          <Generate></Generate>
          : 
          <ViewNotes></ViewNotes>
          }
        </Flex>
      </MantineProvider>
    </React.StrictMode>
  );
}

const theme = createTheme({
  primaryColor: 'muteBlue',
  fontFamily: 'Inter, sans-serif',
  fontSizes: {
    xs: '0.5em',
    sm: '0.875em',
    md: '1em',
    lg: '1.3em',
    xl: '3.75em'
  },
  headings: {
    fontFamily: 'Jomolhari',
    sizes: {
      h1: { fontWeight: '300', fontSize: '1.25em' },
      h2: { fontWeight: '200', fontSize: '1.5em' }
    },
  },
  colors: {
    'muteBlue': [
      '#ecf6ff',
      '#dee8f1',
      '#bfcedc',
      '#9cb3c8',
      '#7f9db6',
      '#6c8eac',
      '#6287a8',
      '#507493',
      '#446785',
      '#335a77'
    ]
  }
});

export default App;
