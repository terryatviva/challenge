import React from 'react';
import {Button, Form} from 'react-bootstrap';

function Survey() {
  return (
    <div style={{ padding: '10px 30px' }}>
        <Form>
          <Form.Group controlId="formGroupName">
            <div>
              <Form.Label>User Name</Form.Label>
            </div>
            <Form.Control size="lg" type="text" placeholder="Enter name" />
          </Form.Group>
          <Form.Group controlId="formGroupDOB">
            <div>
              <Form.Label>Date Of Birth</Form.Label>
            </div>
            <Form.Control type="city" placeholder="Enter City" />
          </Form.Group>
          <Form.Group controlId="formGroupEmail">
            <div>
              <Form.Label>Email address</Form.Label>
            </div>
            <Form.Control type="email" placeholder="Enter email" />
          </Form.Group>
          <Form.Group controlId="formGroupCity">
            <div>
              <Form.Label>City</Form.Label>
            </div>
            <Form.Control type="text" placeholder="Enter City" />
          </Form.Group>
          <Form.Group controlId="formGroupCountry">
            <div>
              <Form.Label>Country</Form.Label>
            </div>
            <Form.Control type="text" placeholder="Enter country" />
          </Form.Group>
          <Form.Group controlId="formGroupLike">
            <div>
              <Form.Label>What are few things you like about our products</Form.Label>
            </div>
            <Form.Control as="textarea" rows="5" />
          </Form.Group>
          <Form.Group controlId="formGroupDislike">
            <div>
              <Form.Label>What are few things you dislike about our products</Form.Label>
            </div>
            <Form.Control as="textarea" rows="5" />
          </Form.Group>
          <Button variant="primary" type="submit">Submit</Button>
        </Form>
    </div>
  );
}

export default Survey;