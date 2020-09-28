import React, { useEffect, useRef, useState } from 'react';
import { Row, Container, Button } from 'react-bootstrap';
import { Form } from "react-bootstrap";
import axios from "axios"

function Index() {
    let [formData, setFormData]  = useState({});
    let [completed, setCompleted]  = useState(false);
    let [error, setError]  = useState(false);
    const firstFetch = useRef(true)
    useEffect(()=> {
        if (firstFetch.current){
            let formSchema = {
                'name':'',
                'email': '',
                'city': '',
                'country':'',
                'DOB':'',
                'like':'',
                'dislike': ''
            }
            setFormData(formSchema);
            firstFetch.current = false
        }
    }, [])

    const submitForm = (e) => {
        e.preventDefault();
        let isValidate = validate();
        if (isValidate) {
            axios.post("/submit", {
                data: JSON.stringify(formData),
            }).then(response => {
                if (response.data.message === undefined)
                    setCompleted(true)
            })
        }
    };

    const validate = () => {
        let out = true;
        Object.keys(formData).forEach((key) => {
            if (formData[key] === '') {
                setError('All fields are required');
                out = false
            }
        });
        return out
    }

    const updateData=(field, data)=>{
        let temp_obj = formData;
        temp_obj[field] = data;
        setFormData(temp_obj)
    };
    return (
    <>
        {!completed ?  <Container style={{padding: '0 30px'}}>
            <Row>
                <h2>User Survey</h2>
                We are collecting our customers' views to provide the better quality products. Please provide us your
                opinion about our products by filling the following form:
            </Row>
            <div style={{ padding: '10px 40px' }}>
                {error && <div style={{color: 'red'}}>{error}</div>}
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
                    <Form.Control type="date" placeholder="Enter Date Of Birth" onChange={(e) => updateData('DOB', e.target.value)} />
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