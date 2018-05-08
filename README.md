# Online Store  

A website created by using Django framework for practice python and html demo on Heroku [101SHOP](https://ml101-shop.herokuapp.com/).  

## Website Introduction  

### Home  
* At the homepage of website, there has a carousel display all products picture for customer.  
* Sidebar at the left provide category switch of products. Customer can select the category they liked to shopping or view all products by click all button.  
* (Future) Only display the hot products in carousel.  

### Product Category  
* If customer want buy something they liked, they can click `Add to Cart` add the product to the cart and checkout fast and easily, or click the product's picture to view details of the product and select quantities of the product they want to buy, then click `Add to Cart` button.  

### Header Bar  
* `101SHOP` link to homepage.  
* If customer doesn't login, there will show `Wellcome guest` right of `101SHOP`, or show `Wellcome customer_name` for login customer.  
* `Order Dashboard` showed if login account is staff.  
* `Product Dashboard` showed if login account is staff.  
* `Cart` for all user to add product they want to buy and checkout finally.  
* `Account Center` for all user to view and edit their account's data, or check their order schedule.  
* `Login/Signup` showed if user doesn't login.  
* `Logout` showed if user login.  

### Order Dashboard  
* List all orders of all user.  
* 5 buttons at the top can switch order display by order status.  
* Order ID link to the detail of order's `Receiver` `Contact Number` `Address` `Items`.  
* Staff can click the `Next` button to change the order status when they process the order.  

### Product Dashboard  
* `Add Category` for staff new a product category.  
* `Add Product` for staff new a product for a exist category.  
* The icon beside product category of the left sidebar can edit category name or delete the category.  
* `Edit` button can change the product's detail.  
* `Delete` button can delete the product.  

### Cart  
* If customer doesn't add any product into the cart, there will display `No product in cart`.  
* Customer can add or minus the quantities of product, the quantity least is 1.  
* `Trash Can` icon at the right of all product use to remove product from cart.  
* `Pay on Delivery` is the default of payment. Customer can choose `Credit Card` if they want.  
* `Credit Card` payment now supported by Paypal only, and use developer mode for test function.  
   When checkout order will show the paypal payment website in sandbox.  
   After login and pay successful by using foo-buyer@email.com paypal test account, click return shop link will show the order processing message.  
   If customer cancel the payment, there will display payment canceled message.  
   The order's payment status will change to True after paypal check the payment successful and post a signal to shop.  
* `Checkout` toggle a Modal window for customer to check all of order's `items` `Payment Method` `Receiver Name` `Contact Number` `Address` and confirm the order, or click the other side of Modal window to cancel checkout.  

### Account Center  
* Order ID link to the detail of order's `Receiver` `Contact Number` `Address` `Items`.  
* (Future) User can cancel the order in account center when order status is `PENDING`.  
* (Future) User can edit their personal data at the account canter.  

### Login / Sign Up  
* Login a exist account at `Login` tab.  
* Singup a new account at `Login Up` tab.  
* (Future) Increase the signup form, and improve the login / signup flow to avoid some bug.  
* (Future) Send a verify email to new signup user, they need to verify their email for checkout.  

### Logout  
* Logout the login account and redirect to homepage.  
