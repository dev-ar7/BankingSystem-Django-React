import React from "react";
import NavBar from "./Navbar";
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import '../Static/Css/LogIn.css';


function LogIn() {


    return (
        <>
            <NavBar />
            <div className="login">
                <h1 className="heading">LogIn</h1>
                <Card className="form mb-5" style={{ width: '50rem' }}>
                    <Card.Body>
                        <Form >
                            <Form.Group className="mb-3" controlId="formBasicEmail">
                                <Form.Label>Email address</Form.Label>
                                <Form.Control type="email" placeholder="Enter email" />
                                <Form.Text className="text-muted">
                                    We'll never share your email with anyone else.
                                </Form.Text>
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formBasicPassword">
                                <Form.Label>Password</Form.Label>
                                <Form.Control type="password" placeholder="Password" />
                                <Form.Text className="text-muted">
                                    You Should remember your password, There's no reset or forgot password option here.
                                </Form.Text>
                            </Form.Group>
                            <Button className="btn" variant="primary" type="submit">
                                Submit
                            </Button>
                        </Form>
                        <p className="mt-3">Don't have an account? <a href='/signup'>SignUp</a></p>
                    </Card.Body>
                </Card>
            </div>
        </>
    );
}


export default LogIn;