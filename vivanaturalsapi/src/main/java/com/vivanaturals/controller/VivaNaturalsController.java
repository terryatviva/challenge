package com.vivanaturals.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.vivanaturals.entity.Feedback;
import com.vivanaturals.service.VivaNaturalsService;

@RestController
public class VivaNaturalsController {
	
	@Autowired
	private VivaNaturalsService service;
	
	@PostMapping("/feedback")
	public ResponseEntity<Long> saveFeedback(@RequestBody Feedback feedback){
		return new ResponseEntity<Long>(service.saveFeedback(feedback),HttpStatus.CREATED);
	}
	
	@GetMapping("/feedback")
	public ResponseEntity<List<Feedback>> getFeedback(){
		return new ResponseEntity<List<Feedback>>(service.getFeedback(),HttpStatus.OK);
	}
	
}
