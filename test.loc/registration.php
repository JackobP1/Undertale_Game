<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Registration Form</title>
<style>
    body {
        margin: 0;
        padding: 0;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .registration-container {
        text-align: center;
    }

    .input-group {
        margin-bottom: 10px;
    }

    .input-group input {
        width: 400px;
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 30px;
    }

    button {
        padding: 15px 30px;
        font-size: 24px;
        margin-bottom: 10px;
    }
</style>
</head>
<body>

<div class="registration-container">
<?php
    $error_nick_exist = isset($_GET['error_nick_exist']) ? $_GET['error_nick_exist'] : null;
    if ($error_nick_exist !== null) {
        echo $error_nick_exist;
    }
?>
<?php
    $error_email_exist = isset($_GET['error_email_exist']) ? $_GET['error_email_exist'] : null;
    if ($error_email_exist !== null) {
        echo $error_email_exist;
    }
?>
    <form action="index.php" method="post">
        <div class="input-group">
            <input type="text" name="nickname" placeholder="Nick-name">
        </div>
        <div class="input-group">
            <input type="email" name="email" placeholder="E-mail">
        </div>
        <div class="input-group">
            <input type="password" name="password" placeholder="Password">
        </div>
        <button type="submit" name="reg_account">Reg account</button>
        <form action="enter.php" method="post">
        <button type="submit" name="have_account">I have account</button>
        </form>
    </form>
</div>

</body>
</html>


