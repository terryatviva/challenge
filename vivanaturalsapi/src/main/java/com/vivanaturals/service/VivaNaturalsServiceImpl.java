package com.vivanaturals.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.vivanaturals.entity.Feedback;
import com.vivanaturals.repository.VivaNaturalsRepo;

@Service
public class VivaNaturalsServiceImpl implements VivaNaturalsService{

	@Autowired
	private VivaNaturalsRepo repo;
	
	@Override
	public Long saveFeedback(Feedback feedback) {
		Integer id = repo.getId();
		if(id==null) 
			id=1001;
		else
			id++;
		feedback.setId(id);
		repo.save(feedback);
		return 1L;
	}

	@Override
	public List<Feedback> getFeedback() {
		return repo.findAll();
	}	

}
