package com.vivanaturals.service;

import java.util.List;

import com.vivanaturals.entity.Feedback;

public interface VivaNaturalsService {

	Long saveFeedback(Feedback feedback);

	List<Feedback> getFeedback();

}
