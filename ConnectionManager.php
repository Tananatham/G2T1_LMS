<?php
class ConnectionManager {

    public function connect() {
        $servername = 'localhost';
        $username = 'root';
        $password = '';
        $dbname = 'lms_course';
        $port = '3306';

        $pdoObject = new PDO(
            "mysql:host=$servername;dbname=$dbname;port=$port",
            $username,
            $password);

        $pdoObject->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        return $pdoObject;
        
    }
}