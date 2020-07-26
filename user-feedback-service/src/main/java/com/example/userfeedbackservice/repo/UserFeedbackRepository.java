package com.example.userfeedbackservice.repo;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.userfeedbackservice.models.UserFeedback;

public interface UserFeedbackRepository extends JpaRepository<UserFeedback, Long> {

}