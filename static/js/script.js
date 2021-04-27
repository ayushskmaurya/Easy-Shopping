function search(n) {
	let query = document.getElementById("query-" + n).value.trim();
	if(query.length > 0)
		location.href = "/search/" + query;
}

// Checking wether user is logged in.
function is_logged_in() {
	let isLoggedIn = document.getElementById("is-logged-in").innerHTML;
	if(isLoggedIn == "1")
		return true;
	return false;
}

// Adding product to the cart.
function add_to_cart(product_id) {
	if(is_logged_in())
		location.href = "/add_to_cart/" + product_id;
	else
		document.getElementById("login").click();
}

// Adding product to the wishlist.
function add_to_wishlist(product_id) {
	if(is_logged_in())
		location.href = "/add_to_wishlist/" + product_id;
	else
		document.getElementById("login").click();
}

// Show error message if occured
function show_error_msg(div_id, msg_id, msg) {
	document.getElementById(msg_id).innerHTML = msg;
	document.getElementById(div_id).style.display = "block";
}

// Hide error message
function hide_error_msg(div_id, msg_id) {
	document.getElementById(msg_id).innerHTML = "";
	document.getElementById(div_id).style.display = "none";
}

// Login
function login(div_id, msg_id) {
	let email = document.getElementById("login-email").value.trim();
	let pwd = document.getElementById("login-pwd").value;

	let regx = /^([a-zA-Z0-9\._-]+)@([a-zA-Z0-9-]+)(\.[a-z]{2,20})?(\.([a-z]{2,20}))$/;
	if(!regx.test(email))
		show_error_msg(div_id, msg_id, "Please enter valid email.");

	else if(pwd.length === 0) 
		show_error_msg(div_id, msg_id, "Please fill password field.");

	else {
		const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
		$.ajax({
			headers: {'X-CSRFToken': csrftoken},
			url: "/verify_user",
			method: "POST",
			data: {email:email, pwd:pwd},
			success: function(msg) {
				if(msg != "1")
					show_error_msg(div_id, msg_id, msg);
				else
					location.reload();
			}
		});
	}
}

// Registering new user
function register(div_id, msg_id) {
	let name = document.getElementById("reg-name").value.trim();
	let email = document.getElementById("reg-email").value.trim();
	let mob = document.getElementById("reg-mob").value.trim();
	let pwd = document.getElementById("reg-pwd").value;
	let cpwd = document.getElementById("reg-cpwd").value;

	let regx = /^([a-zA-Z0-9\._-]+)@([a-zA-Z0-9-]+)(\.[a-z]{2,20})?(\.([a-z]{2,20}))$/;

	if(name.length === 0)
		show_error_msg(div_id, msg_id, "Please enter valid name.");

	else if(!regx.test(email))
		show_error_msg(div_id, msg_id, "Please enter valid email.");

	else if(!/^\d{10}$/.test(mob))
		show_error_msg(div_id, msg_id, "Please enter valid mobile no.");

	else if(pwd.length === 0) 
		show_error_msg(div_id, msg_id, "Please fill password field.");
	
	else if(pwd != cpwd) 
		show_error_msg(div_id, msg_id, "Passwords do not match.");

	else {
		const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
		$.ajax({
			headers: {'X-CSRFToken': csrftoken},
			url: "/validate_user",
			method: "POST",
			data: {name:name, email:email, mob:mob, pwd:pwd},
			success: function(msg) {
				if(msg != "1")
					show_error_msg(div_id, msg_id, msg);
				else
					location.reload();
			}
		});
	}
}
