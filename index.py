<!doctype html>
<html lang="en">
  <head>
    
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>EditKaro--> editing to sharpness</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  </head>
  <body>
    
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="/">EditKaro</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/aboutus">About us</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/contactus">contact us</a>
              </li>



            </ul>


          </div>
        </div>
      </nav>
      {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        
        {% for category, message in messages %}
          
          <div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>CONGO!</strong> {{ message | safe }}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>
        {% endfor %}
        
      {% endif %}
    {% endwith %}
    <div class="container my-4">
    <h1 class="fs-2 text">EditKaro--> editing to sharpness</h1>
    <form action="/edit" method="post" enctype="multipart/form-data">
    <div class="mb-3">
        <label for="formFile" class="form-label">select an image to edit</label>
        <input class="form-control" type="file" name="file" id="formFile">
      </div>
      <select name ="operation" class="form-select" aria-label="Default select example">
        <option selected>Open this operation</option>
        <option value="sketch">jpg to sketch</option>
        <option value="bgremove">background remove</option>
        <option value="greyscale">jpg to greyscale</option>
      </select>
      <br>
      <button type="submit" class="btn btn-success">Submit</button>
    </form>
    </div>
    <img src="https://source.unsplash.com/featured?technology" alt="okok" align="left">
    
  

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
  </body>
</html>
