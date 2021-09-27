<!DOCTYPE html>
<?php

require_once 'DAO/CourseDAO.php';
$dao = new CourseDAO();
// Form Processing

$contacts = $dao->getCourse();
?>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
<html>
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    </head>
    <body>
    <div class="container p-5">
        <h1>Courses</h1>
            <table class="table">
                <tr>
                    <th scope="col">Course ID</th>
                    <th scope="col">Course Name</th>
                    <th scope="col">Number of class</th>
                    <th scope="col">Number of lesson</th>
                    <th scope="col">Class ID</th>
                    <th scope="col">Course Description</th>
                    <th scope="col">Course Prerequisite</th>
                    <th scope="col">Start Time</th>
                    <th scope="col">End Time</th>
                    <th scope="col">Date Uploaded</th>
                </tr>

                <?php
                    foreach($contacts as $contact) {
                        $id = $contact->getcourse_id();
                        echo "
                            <tr>
                            
                                <td>
                                    {$id}
                                </td>
                                <td>
                                    {$contact->getcourse_name()}
                                </td>
                                <td>
                                    {$contact->gettotal_no_of_class()}
                                </td>
                                <td>
                                    {$contact->gettotal_no_of_lesson()}
                                </td>
                                <td >
                                    {$contact->getclass_id()}
                                </td>
                                <td>
                                    {$contact->getcourse_description()}
                                </td>
                                <td>
                                    {$contact->getcourse_prerequisite()}
                                </td>
                                <td>
                                    {$contact->getstart_time()}
                                </td>
                                <td>
                                    {$contact->getend_time()}
                                </td>
                                <td>
                                    {$contact->getdatetime_uploaded()}
                                </td>
                                </tr>
                        ";
                    }
                ?>

            </table>
            <a class="btn btn-primary" href="course-add.php">Add New Course</a>
        </div>
</div>

<script src="https://js.stripe.com/v3/"></script>
    <script src="{{url_for('static', filename='stripe.js')}}"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.6.0/dist/umd/popper.min.js" integrity="sha384-KsvD1yqQ1/1+IA7gi3P0tyJcT3vR+NdBTt13hSJ2lnve8agRGXTTyNaBYmCR/Nwi" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.min.js" integrity="sha384-nsg8ua9HAw1y0W1btsyWgBklPnCUAFLuTMS2G72MMONqmOymq585AcH49TLBQObG" crossorigin="anonymous"></script>

    </body>
</html>