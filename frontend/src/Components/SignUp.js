import React from "react";
import NavBar from "./Navbar";
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import '../Static/Css/Signup.css';


function SignUp() {
    return (
        <>
            <NavBar />
            <div className="signup">
                <h1 className="heading mb-3">SignUp</h1>
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
                            <Form.Group className="mb-3" controlId="formBasicFirstName">
                                <Form.Label>First Name</Form.Label>
                                <Form.Control type="text" placeholder="First Name" />
                            </Form.Group>
                            <Form.Group className="mb-3" controlId="formBasicLastName">
                                <Form.Label>Last Name</Form.Label>
                                <Form.Control type="text" placeholder="Last Name" />
                            </Form.Group>
                            <Form.Group className="mb-3" controlId="formBasicAccountType">
                                <Form.Label>Account Type</Form.Label>
                                <Form.Control type="text" placeholder="Account Type" value='savings' />
                                <Form.Text className="text-muted">
                                    Account Type you want to open, Like 'Savings' or 'Current' Account. Default is 'Savings'.
                                </Form.Text>
                            </Form.Group>
                            <Button className="btn" variant="primary" type="submit">
                                Submit
                            </Button>
                        </Form>
                        <p className="mt-3">Already have an account? <a href='/'>LogIn</a></p>
                    </Card.Body>
                </Card>
            </div>
        </>
    );
}


export default SignUp;