import React from 'react'
import {Box, Flex, Container} from '@chakra-ui/react'

const Navbar = () => {
  return (
    <Container maxW={"900px"}>
        <Box px={4} my={4} borderRadius={5}>
            {/* Left side */}
            <Flex></Flex>
            {/* Right side */}
            <Flex></Flex>
        </Box>
    </Container>
  )
}

export default Navbar
