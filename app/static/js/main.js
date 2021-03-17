function close_message_board(){
    console.log(this);
    message_board = document.getElementById("message_panel")
    console.log(message_board)
    message_board.style.display="none";
    
    // current_label = document.getElementById('order_btn').innerHTML
    // if (current_label == 'Order'){
    //     document.getElementById('order_btn').innerHTML='Cancel'
    // }
    // else{
    //     document.getElementById('order_btn').innerHTML='Order'
    // }
};

function change_label(el){
    
    if (el.innerHTML == "More"){
        el.classList.add("warning")
        el.innerHTML = "Cancel"
    }
    else{
        el.innerHTML = "More"
    }
};

function change_content(el){
    cancel_btn = document.getElementById("cancel_btn")
    title_holder = document.getElementById("title_holder")
    image_holder = document.getElementById("img_div")
    specs_div = document.getElementById("specs_div")
    order_div = document.getElementById("order_div")
    price = document.getElementById("price")


    if (el.innerHTML == "More"){
        el.innerHTML = "Order";
        title_holder.innerHTML = "Specifications";
        image_holder.style.display="none";
        price.style.display="none";
        specs_div.style.display="block";
        cancel_btn.style.display="none";
        
    }
    else if(el.innerHTML == "Order"){
        el.innerHTML = "Confirm";
        cancel_btn.style.display="none";
        title_holder.innerHTML = "Enter Details";
        specs_div.style.display="none";
        order_div.style.display="block";
    }
    else if (el.innerHTML == "Confirm"){
        console.log("Confirm");
        el.innerHTML = "Done";
        title_holder.innerHTML = "Done !"
    }
    else if (el.innerHTML == "Done"){
        console.log("Done");
        el.innerHTML="More"
        title_holder.innerHTML = "Title"
    }


    
};


function set_description(){
    var selection = document.getElementById("product_selector").value;

    var iphone_section = document.getElementById("iphone_description");
    var ipad_section = document.getElementById("ipad_description");
    var laptop_section = document.getElementById("laptop_description");
    var accessory_section = document.getElementById("accessory_description");
    var form = document.getElementById("product_form");

    if (selection == "iphone"){
        iphone_section.style.display="block";
        ipad_section.style.display="none";
        laptop_section.style.display="none";
        accessory_section.style.display="none";
        
        
    }
    else if (selection =="ipad"){
        iphone_section.style.display="none";
        ipad_section.style.display="block";
        laptop_section.style.display="none";
        accessory_section.style.display="none";
        
    }

    else if (selection =="laptop"){
        iphone_section.style.display="none";
        ipad_section.style.display="none";
        laptop_section.style.display="block";
        accessory_section.style.display="none";
        
    }

    else if (selection == "accessories"){
        iphone_section.style.display="none";
        ipad_section.style.display="none";
        laptop_section.style.display="none";
        accessory_section.style.display="block";
        
    }

};

let active_index = 0;

var boards = document.getElementsByClassName("flash_board");
console.log("The number of boards is : ", boards.length)

function show_flash_boards(int_input){
    var i;
    var boards = document.getElementsByClassName("flash_board");
    if (int_input > boards.length) {slideIndex = 1; active_index=slideIndex}

    if (int_input < 1) {slideIndex = boards.length ; active_index=slideIndex}

    if (int_input < boards.length) {
        slideIndex = int_input;
        active_index=slideIndex
    }

    for (i =0; i < boards.length; i++){
        boards[i].style.display = "none"
        boards[slideIndex].classList.remove("showup")
    }

    boards[slideIndex].style.display = "block";
    boards[slideIndex].classList.add("showup");
    
}



function next_board(){
    let next_boards = document.getElementsByClassName("flash_board");
    console.log("executing next_board, boards are: ",next_boards);

    for (i =0; i < next_boards.length; i++){
        next_boards[i].style.display == "none";
        console.log("board is turned off");
    }

    console.log("active index is:", active_index);
    
    if (active_index == 0){
        active_index = 1;
        show_flash_boards(active_index)
        active_index ++;
    }
    else if (active_index == 1){
        show_flash_boards(active_index)
        active_index ++;
    }
    else if (active_index == 2){
        show_flash_boards(active_index)
        active_index ++;
    }
    else{
        active_index = 0;
        show_flash_boards(active_index)
        active_index ++;
    }
}

// var slideIndex = 0;
// show_flash_boards(slideIndex);



$(document).ready(function(){
    let tick = 0;
    show_flash_boards(tick)

    let clock = setInterval(()=>{
        console.log("ticks", tick++);
        
        if (tick == 3){
            clearInterval(clock);
            tick = 0
            console.log("stoping to default");
            show_flash_boards(tick)
            active_index = tick
            console.log("active index is :", active_index);
        }
        else{
            show_flash_boards(tick);
            active_index = tick
            console.log("active index is :", active_index);
        }

        

    }, 2500);
});



function switch_page(arg_string){
    console.log(arg_string);
    url_string = "/products/"+ arg_string
    console.log(url_string);
    window.location.href = url_string
}



$('.mySlides').on('swipeleft', function (){
    console.log("swipped left")
});

$('.mySlides').on('swiperight', function (){
    console.log("swipped right")
});