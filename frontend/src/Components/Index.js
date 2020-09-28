import React, { useEffect, useState } from 'react';
import { Row, Container, Button } from 'react-bootstrap';
import { Form } from "react-bootstrap";
import axios from "axios"

function Index() {
    let [formData, setFormData]  = useState({});
    let [completed, setCompleted]  = useState(false);
    const submitForm = (e) => {
        e.preventDefault();
        console.log('submit form', formData);
        axios.post("/submit", {
        data: JSON.stringify(formData),
    })
        .then(response => setCompleted(true))
    };

    const updateData=(field, data)=>{
        let temp_obj = formData;
        temp_obj[field] = data;
        setFormData(temp_obj)
    };
    return (
    <>
        {!completed ?  <Container style={{padding: 30}}>
            <Row>
                We are collecting our customers' views to provide the better quality products. Please provide us your
                opinion about our products by filling the following form:
            </Row>
            <div style={{ padding: '10px 0' }}>
                <Form onSubmit={submitForm}>
                    <Form.Group controlId="formGroupName">
                    <div>
                      <Form.Label>User Name</Form.Label>
                    </div>
                    <Form.Control size="lg" type="text" placeholder="Enter name" onChange={(e) => updateData('name', e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="formGroupDOB">
                    <div>
                      <Form.Label>Date Of Birth</Form.Label>
                    </div>
                    <Form.Control type="text" placeholder="Enter Date Of Birth" onChange={(e) => updateData('DOB', e.target.value)} />
                    </Form.Group>
                    <Form.Group controlId="formGroupEmail">
                    <div>
                      <Form.Label>Email address</Form.Label>
                    </div>
                    <Form.Control type="email" placeholder="Enter email" onChange={(e) => updateData('email', e.target.value)} />
                    </Form.Group>
                    <Form.Group controlId="formGroupCity">
                    <div>
                      <Form.Label>City</Form.Label>
                    </div>
                    <Form.Control type="text" placeholder="Enter City" onChange={(e) => updateData('city', e.target.value)} />
                    </Form.Group>
                    <Form.Group controlId="formGroupCountry">
                    <div>
                      <Form.Label>Country</Form.Label>
                    </div>
                    <Form.Control type="text" placeholder="Enter country" onChange={(e) => updateData('country', e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="formGroupLike">
                    <div>
                      <Form.Label>What are few things you like about our products</Form.Label>
                    </div>
                    <Form.Control as="textarea" rows="5" onChange={(e) => updateData('like', e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="formGroupDislike">
                    <div>
                      <Form.Label>What are few things you dislike about our products</Form.Label>
                    </div>
                    <Form.Control as="textarea" rows="5" onChange={(e) => updateData('dislike', e.target.value)} />
                    </Form.Group>
                    <Button variant="primary" type="submit">Submit</Button>
                </Form>
            </div>
        </Container>
            :
            <div style={{
                textAlign: 'center',
                fontSize: 40,
                fontWeight: 600,
                padding: 50
            }}>
                Thank you
            </div>
        }
    </>
  );
}

export default Index;