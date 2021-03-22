import React , {useState, useRef} from 'react';
import axios from 'axios';
import { Modal, Button } from 'react-bootstrap';
import FeedbackForm from './feedback-form.js';
import FeedbackModal from './feedback-modal.js';
export default function Main(){
  const [modalIsShown, setModalIsShown]=useState(false);
  const formRef = useRef();
  function submitFeedback( data ){
    axios.post('/feedback', data)
      .then((rs)=>{
        setModalIsShown(true);
        formRef.current.clearData()
        console.log(rs);
      })
      .catch((err)=>{
        console.log(err);
      })
  }
  const handleClose = () => setModalIsShown(false);
  return(
    <div>
      <h3>We would love to hear from you! Please take a moment to let us know about your experience.</h3>
      <hr/>
      <FeedbackForm ref={formRef} submitFunc={submitFeedback}/>
      <FeedbackModal handleClose={handleClose} modalIsShown={modalIsShown}/>
    </div>
  )
}