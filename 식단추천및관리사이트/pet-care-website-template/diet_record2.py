<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <link rel="shortcut icon" href="/img/favicon.ico">

    <link rel="stylesheet" href="/css/header.css?20211211">
    <link rel="stylesheet" href="/css/lecture_edit.css?20211211">

    <script type="text/javascript" src="/js/lecture/lecture_edit.js?20211211">
    </script>

    <title>Andthen</title>
</head>

<body>
    <%@ include file="/header.jsp" %>  

    <%
        Object user_obj = request.getSession().getAttribute("USER");
        if(user_obj == null || user_obj.equals("") || user_obj.equals("null")) { // 로그인 체크
            out.println(MovePage("잘못된 접근입니다.", "/"));
            return;
        }
        String[][] result = andthenDB.GetDataInLecture("lecture_idx, creator_idx, thumbnail, name, shortdesc, descript", "creator_idx=\"" + (String)user_obj + "\" AND lecture_idx=\"" + request.getParameter("lecture") + "\"");
        if(andthenDB.isError() || andthenDB.GetRowCount() <= 0) {
            out.println(MovePage("잘못된 접근입니다.", "/"));
            return;
        }
        
        String timeStamp = new java.text.SimpleDateFormat("yyyy.MM.dd.HH.mm.ss").format(new java.util.Date());
    %>

    <div class="container">
            <form action="/lecture/lecture_update.jsp" method="post" enctype="multipart/form-data" onsubmit="return checkEmpty();">
                <input type="hidden" id="lecture" name="lecture" value="<%=request.getParameter("lecture")%>">

                    <fieldset class="photo">
                        <img src="<%=result[0][2]%>?<%=timeStamp%>" width="230px" height="230px" id="photo_real">
                        <input type="file" id="profile_photo" name="profile_photo">
                    </fieldset>
                    <script type="text/javascript" src="/js/lecture/preview_lecture.js?20211211"></script>
                
                    <fieldset class="lecture_info">
                        <table class="detail_table">
                            <tr>
                                <td>제목</td>
                                <td><input type="text" id="lecture_title" value="<%=result[0][3]%>" name="lecture_title"></td>
                            </tr>
                            <tr>
                                <td>설명</td>
                                <td><input type="text" id="simple_intro" value="<%=result[0][4]%>" name="simple_intro"></td>
                            </tr>
                        </table>
                    </fieldset>
               
  
<br><br>
<br><br>    
<br><br>
<br><br>
&nbsp;
        <fieldset class="class_area">
            <h4>강의 소개</h4>
            <textarea id="lecture_intro" name="lecture_intro" style="resize: none;"><%=result[0][5]%></textarea>
        </fieldset>
<br>
        <fieldset class="curri" height:300px>
            <h4>커리큘럼 수정 페이지 ▼</h4>
            <input type="hidden" id="cur_count" name="cur_count" value="0">
            <ul id="curriculum">
                <%
                    // 커리큘럼 가져오기
                    result = andthenDB.GetDataInCurriculum("curriculum_idx, name", "lecture_idx=\"" + request.getParameter("lecture") + "\" ORDER BY LIST"); 
                    if(andthenDB.isError()) {
                        out.println(MovePage("잘못된 접근입니다.", "/"));
                        return;
                    }
                    
                    int curr_cnt = andthenDB.GetRowCount();
                    for(int i = 0; i < curr_cnt; i++) {
                        String[][] lesson = andthenDB.GetDataInLesson("video", "curriculum_idx=\"" + result[i][0] + "\""); 
                        if(!(andthenDB.isError()) || andthenDB.GetRowCount() >= 1) {
                            %> <script> addCurList("<%=result[i][1]%>", "<%=lesson[0][0]%>"); </script> <%
                        }
                    }
                %>
            </ul>
            <input type="button" id="up_down_button" value="+" onclick="addCurListEmpty()">    
            <input type="button" id="up_down_button" value="-" onclick="deleteCurList()">
        </fieldset> <br>

        <input type="submit" id="edit_button" value="완료">

    </div>

    <iframe src="/footer.html" width="100%" height="10%" frameborder=0 framespacing=0 marginheight=0 marginwidth=0
        scrolling=no vspace=0></iframe>
</body>

</html>