
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*"%>
<h1>DB</h2>
<%
        Connection conn=null;
        try{
                String Url="jdbc:mysql://3tier_db/tomdb";
                String Id="tomuser";
                String Pass="tompassword";

                Class.forName("com.mysql.jdbc.Driver");
                conn=DriverManager.getConnection(Url,Id,Pass);
                out.println("was-db Connection Success!");
        }catch(Exception e) {
                e.printStackTrace(); 
}
%>

