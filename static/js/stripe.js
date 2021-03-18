console.log("Sanity check");

// Get Stripe publishable key
fetch("/boutique/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);
    console.log('fetch 1 reached');
    //Event handler
    document.querySelector("#btnVisa").addEventListener("click", () => {
        // Get Checkout Session ID
        fetch("/boutique/create-checkout-session/")
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
