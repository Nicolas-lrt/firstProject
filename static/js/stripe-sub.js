console.log("Sanity check");

//Get stripe publishable key
fetch("/projets/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  console.log('fetch 1 reached');
  //Event handler
  document.querySelector("#payBtn").addEventListener("click", () => {
      // Get Checkout Session ID
      fetch("/projets/create-checkout-session/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
          console.log(res);
      });
  });
});