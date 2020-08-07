package com.vivanaturals.filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletResponse;

import org.springframework.context.annotation.Configuration;

@Configuration
public class CorsFilter implements Filter{

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		
		HttpServletResponse res = (HttpServletResponse) response;
        
        res.setHeader("Access-Control-Allow-Origin", "*");
        res.setHeader("Access-Control-Allow-Headers","Origin, X-Requested-With, Content-Type, Authorization");
        res.setHeader("Access-Control-Allow-Methods",
                "DELETE, GET, POST, PUT");
        res.setHeader("Vary", "Origin");
        res.setHeader("Access-Control-Request-Method", "Access-Control-Request-Headers");
        chain.doFilter(request, response);
	}	
	
}
