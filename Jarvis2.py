@import url('https://fonts.googleapis.com/css2?family=Ubuntu&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Ubuntu&family=Varela+Round&display=swap');
body{
    background-color: antiquewhite;

}
*{
    margin: 0;
    padding: 0;
}
nav{
    font-family:'Ubuntu', sans-serif;
}

nav ul{
    display: flex;
    list-style-type: none;
    height:65px;
    background-color: black;
    align-items: center;
    color: white;
}
nav ul li{
    padding:0 12px ;
}

.brand img {
    width: 48px;
    padding:0 8px;
}
.brand {
    display: flex;
    align-items: center;
    font-weight: bolder;
    font-size:1.3rem;
}

.container{
    min-height: 72vh;
    background-color: black;
    color:white;
    font-family:  'Varela Round', sans-serif;
    display: flex;
    margin: 23px auto;
    width: 70%;
    border-radius: 12px;
    padding:34px;
    background-image:url("bg.jpg");
    
    
}
.bottom {
    position: sticky;
    height: 100px;
    background-color: black;
    color: white;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;



}
.icons {
    margin-top: 14px;
}
.icons i{
    cursor: pointer;
}
#myProgressBar{
    width:80vw;
}
.songItem {
    height: 50px;
    display: flex;
    background-color: white;
    width: 80%;
    color: black;
    margin: 12px 0;
    justify-content: space-between;
    align-items:center;
    border-radius: 34px;

}
.songItem img{
    width:23px;
    margin: 0 23px;
    
}
.timestamp{
    margin: 0 23px;

}
