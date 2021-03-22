import React , {useState} from 'react';
import { Modal, Button } from 'react-bootstrap';
export default function FeedbackModal( props ){
  let { handleClose, modalIsShown } = props;
  return(
    <Modal show={modalIsShown} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Thank you!</Modal.Title>
      </Modal.Header>
      <Modal.Body>Your Feedback matter to us most. Thank you for taking the time to fill-up the form!</Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          Close
        </Button>
      </Modal.Footer>
    </Modal>
  )
}