package com.vivanaturals.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.vivanaturals.entity.Feedback;

@Repository
public interface VivaNaturalsRepo extends JpaRepository<Feedback, Long>{
	
	@Query("select max(id) from Feedback")
	public Integer getId();
}
