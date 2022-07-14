import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import '../Static/Css/NavBar.css';


function NavBar() {

    const navigate = useNavigate();

    const onClickHome = () => {
        navigate('/');
    }

    const onClicksignUp = () => {
        navigate('/signup');
    }

    return (
        <>
            <Navbar collapseOnSelect expand="lg" >
                <Container>
                    <Navbar.Brand onClick={onClickHome}>RBank</Navbar.Brand>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link onClick={onClickHome}>Home</Nav.Link>
                    </Nav>
                    <Nav>
                        <Nav.Link onClick={onClicksignUp}>SignUp</Nav.Link>
                        <Nav.Link eventKey={2} href="#memes">
                            Contact
                        </Nav.Link>
                    </Nav>
                    </Navbar.Collapse>
                </Container>
                </Navbar>
        </>
    );
}


export default NavBar;