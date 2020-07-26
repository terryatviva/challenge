package com.example.userfeedbackservice.models;

import java.time.LocalDateTime;
import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class UserFeedback {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	private String name;

	private Date dateOfBirth;

	private String email;

	private String country;

	private String city;

	private String thingsLiked;

	private String thingsDisliked;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}


	public Date getDateOfBirth() {
		return dateOfBirth;
	}

	public void setDateOfBirth(Date dateOfBirth) {
		this.dateOfBirth = dateOfBirth;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getCountry() {
		return country;
	}

	public void setCountry(String country) {
		this.country = country;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getThingsLiked() {
		return thingsLiked;
	}

	public void setThingsLiked(String thingsLiked) {
		this.thingsLiked = thingsLiked;
	}

	public String getThingsDisliked() {
		return thingsDisliked;
	}

	public void setThingsDisliked(String thingsDisliked) {
		this.thingsDisliked = thingsDisliked;
	}

	@Override
	public String toString() {
		return "Feedback [id=" + id + ", name=" + name + ", dateOfBirth=" + dateOfBirth + ", email=" + email
				+ ", country=" + country + ", city=" + city + ", thingsLiked=" + thingsLiked + ", thingsDisliked="
				+ thingsDisliked + "]";
	}

}
