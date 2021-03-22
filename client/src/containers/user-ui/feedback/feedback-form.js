import axios from 'axios';
import React, {useState,useEffect, forwardRef, useImperativeHandle } from 'react';
import {Form, Button, Col, Row} from 'react-bootstrap';

// using forwardRef to let the parent component access some of the component function
export default forwardRef ((props, ref) => {
  let { submitFunc } = props;

  const [name, setName] = useState("");
  const [birth_date, setBirthDate] = useState("");
  const [email_address, setEmailAddress] = useState("");
  const [countries, setCountries] = useState([]);
  const [country, setCountry] = useState("");

  const [cities, setCities] = useState([]);
  const [city, setCity] = useState("");

  const [good_comment, setGoodComment] = useState("");
  const [bad_comment, setBadComment] = useState("");
  // declaring function that will be available to the parent
  // useful after successfully submitting the form 
  useImperativeHandle(
    ref,
    () => ({
        clearData() {
          clearInput()
        }
    }),
  )
  // clear all the states(except countries) and input values
  function clearInput(){
    setName("");
    setBirthDate("");
    setEmailAddress("");
    setCountry("");
    setCities([]);
    setCity("");
    setGoodComment("");
    setBadComment("");
  }
  // initialize countries
  useEffect(()=>{
    axios.get('https://countriesnow.space/api/v0.1/countries/codes')
    .then((rs)=>{
      setCountries(rs.data.data);
    })
  },[]);
  function submitFeedback(ev){
    ev.preventDefault();
    submitFunc(
      {
        'name' : name, 
        'birth_date' : birth_date,
        'email_address' : email_address,
        'country' : country,
        'city' : city,
        'good_comment' : good_comment,
        'bad_comment' : bad_comment,
      }
    );
    
  }
  function countryOptionLists(){
    return countries.map((item,idx)=>{
      let value = item.name.toLowerCase();
      return (<option value={value} key={item.code}>{item.name}</option>)      
    });
  }
  function cityOptionLists(){
    return cities.map((item,idx)=>{
      let value = item.toLowerCase();
      return (<option key={idx} value={value}>{item}</option>)
    })
  }
  function onChangeCountryInput(ev){
    let { value } = ev.target;
    setCountry(value);
    axios.post('https://countriesnow.space/api/v0.1/countries/cities', {'country' : value})
        .then((rs)=>{
          let cities = rs.data.data;
          setCities(cities);
          // console.log(cities);
        })
  }
  return(
      <Form onSubmit={submitFeedback}>
        <Row>
          <Col>
            <Form.Group>
              <Form.Label>Name</Form.Label>
              <Form.Control required type="text" placeholder="Enter your name" value={name} onChange={ev=>setName(ev.target.value)}/>
            </Form.Group>
          </Col>
          <Col>
            <Form.Group>
              <Form.Label>Birth date</Form.Label>
              <Form.Control required type="date" placeholder="Enter your birth date" value={birth_date} onChange={ev=>setBirthDate(ev.target.value)}/>
            </Form.Group>
          </Col>
          
        </Row>
        <Form.Group>
          <Form.Label>Email address</Form.Label>
          <Form.Control required type="email" placeholder="Enter your email" value={email_address} onChange={ev=>setEmailAddress(ev.target.value)}/>
          {/* <Form.Text className="text-muted"> We'll never share your email with anyone else.</Form.Text> */}
        </Form.Group>
        <Row>
          <Col>
            <Form.Group>
              <Form.Label>Country</Form.Label>
              <Form.Control as="select" className="form-control" required  value={country} onChange={onChangeCountryInput}>
                <option value="" disabled>Please select a country</option>
                { countryOptionLists() }
              </Form.Control>
            </Form.Group>
          </Col>
          <Col>
            <Form.Group>
              <Form.Label>City</Form.Label>
              <Form.Control as="select" className="form-control" required  value={city} onChange={ev=>setCity(ev.target.value)}>
                <option value="" disabled>Please select a city</option>
                { cityOptionLists() }
              </Form.Control>
            </Form.Group>
          </Col>
        </Row>
        <Form.Group controlId="exampleForm.ControlTextarea1">
          <Form.Label>What did you enjoy most about your experience?</Form.Label>
          <Form.Control required as="textarea" rows={3} value={good_comment} onChange={ev=>setGoodComment(ev.target.value)} />
        </Form.Group>
        <Form.Group controlId="exampleForm.ControlTextarea1">
          <Form.Label>What, if any, products, services, or features are we missing?</Form.Label>
          <Form.Control required as="textarea" rows={3} value={bad_comment} onChange={ev=>setBadComment(ev.target.value)}/>
        </Form.Group>
        <div className="text-right">
          <Button variant="primary" type="submit">
            Submit
          </Button>
        </div>
      </Form>
  )
});