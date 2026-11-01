FAQ_CATEGORIES = {
    "General": "General business information",
    "Contact": "Contact and support information", 
    "Policy": "Company policies and procedures",
    "Shipping": "Shipping and delivery information",
    "Payment": "Payment and billing information",
    "Orders": "Order management and tracking",
    "Account": "Account management and settings",
    "Products": "Product information and availability",
    "Services": "Additional services offered",
    "Programs": "Loyalty and special programs",
    "Pricing": "Pricing and discount information",
    "Issues": "Problem resolution and support",
    "Security": "Security and privacy information",
    "Support": "Technical and customer support"
}

SAMPLE_FAQS = [
    {
        "question": "What are your business hours?",
        "answer": "We are open Monday through Friday, 9 AM to 6 PM EST.",
        "category": "General",
        "keywords": ["hours", "timing", "schedule"]
    },
    {
        "question": "Do you have a mobile app?",
        "answer": "Yes! Our mobile app is available for both iOS and Android devices. Download it from the App Store or Google Play.",
        "category": "General",
        "keywords": ["app", "mobile", "ios", "android"]
    },
    {
        "question": "Do you have physical stores?",
        "answer": "We currently operate online only, but have showrooms in New York, Los Angeles, and Chicago for product viewing.",
        "category": "General",
        "keywords": ["stores", "locations", "physical", "showroom"]
    },
    {
        "question": "What are your holiday hours?",
        "answer": "During holidays, we may have modified hours. Check our website or call ahead for current holiday schedule.",
        "category": "General",
        "keywords": ["holidays", "seasonal hours", "modified schedule"]
    },
    {
        "question": "How can I contact support?",
        "answer": "You can reach our support team via email at support@example.com or call us at 1-800-123-4567.",
        "category": "Contact",
        "keywords": ["support", "contact", "help", "phone", "email"]
    },
    {
        "question": "How do I contact corporate sales?",
        "answer": "For bulk corporate orders, email corporatesales@example.com or call 1-800-987-6543 for dedicated support.",
        "category": "Contact",
        "keywords": ["corporate", "business", "enterprise", "B2B"]
    },
    {
        "question": "What is your return policy?",
        "answer": "We offer a 30-day return policy for unused items in original packaging.",
        "category": "Policy",
        "keywords": ["return", "refund", "money back"]
    },
    {
        "question": "What is your privacy policy?",
        "answer": "We protect your personal information and never share it with third parties without your consent. See our full privacy policy for details.",
        "category": "Policy",
        "keywords": ["privacy", "data protection", "personal information"]
    },
    {
        "question": "Do you price match?",
        "answer": "Yes, we price match authorized retailers within 14 days of purchase. Contact us with the competitor's current price.",
        "category": "Policy",
        "keywords": ["price match", "competitor pricing", "best price"]
    },
    {
        "question": "What is your warranty policy?",
        "answer": "All products come with a 1-year manufacturer warranty covering defects in materials and workmanship.",
        "category": "Policy",
        "keywords": ["warranty", "guarantee", "protection", "coverage"]
    },
    {
        "question": "What is your environmental policy?",
        "answer": "We use eco-friendly packaging, carbon-neutral shipping, and partner with sustainable suppliers. See our sustainability page for details.",
        "category": "Policy",
        "keywords": ["environment", "green", "sustainable", "eco-friendly"]
    },
    {
        "question": "What is your price adjustment policy?",
        "answer": "We offer price adjustments within 7 days of purchase if the item goes on sale. Contact customer service with your order number.",
        "category": "Policy",
        "keywords": ["price adjustment", "sale price", "price drop"]
    },
    {
        "question": "Do you price match online retailers?",
        "answer": "We price match major authorized online retailers. Contact us with the competitor's current price and website.",
        "category": "Policy",
        "keywords": ["online price match", "internet pricing", "competitor"]
    },
    {
        "question": "What is your restocking fee?",
        "answer": "Returns may incur a 10% restocking fee for opened items. Unopened items in original packaging have no restocking fee.",
        "category": "Policy",
        "keywords": ["restocking fee", "return charge", "restock cost"]
    },
    {
        "question": "What is your cancellation policy for custom orders?",
        "answer": "Custom orders cannot be cancelled after 24 hours of placement as production begins immediately.",
        "category": "Policy",
        "keywords": ["custom order", "personalized item", "cancellation"]
    },
    {
        "question": "How long does shipping take?",
        "answer": "Standard shipping takes 5-7 business days. Express shipping is available for 2-3 business days.",
        "category": "Shipping",
        "keywords": ["shipping", "delivery", "time", "duration"]
    },
    {
        "question": "Do you offer international shipping?",
        "answer": "Yes, we ship to most countries worldwide. International shipping typically takes 10-15 business days.",
        "category": "Shipping",
        "keywords": ["international", "worldwide", "global"]
    },
    {
        "question": "What are your shipping costs?",
        "answer": "Standard shipping is $4.99 for orders under $50. Express shipping is $12.99. Orders over $50 qualify for free standard shipping.",
        "category": "Shipping",
        "keywords": ["cost", "fees", "shipping price", "delivery charge"]
    },
    {
        "question": "Do you offer white glove delivery?",
        "answer": "Yes, white glove delivery including assembly and placement is available for large furniture items.",
        "category": "Shipping",
        "keywords": ["white glove", "premium delivery", "assembly service"]
    },
    {
        "question": "What payment methods do you accept?",
        "answer": "We accept all major credit cards, PayPal, and Apple Pay.",
        "category": "Payment",
        "keywords": ["payment", "credit card", "paypal", "apple pay"]
    },
    {
        "question": "How do I apply a discount code?",
        "answer": "Enter your discount code in the 'Promo Code' field at checkout and click 'Apply'. The discount will be reflected in your total.",
        "category": "Payment",
        "keywords": ["discount", "promo code", "coupon", "voucher"]
    },
    {
        "question": "How do I use a gift card?",
        "answer": "Enter your gift card code in the 'Gift Card' field at checkout. Gift cards can be combined with other payment methods.",
        "category": "Payment",
        "keywords": ["gift card", "voucher", "certificate", "redeem"]
    },
    {
        "question": "What currencies do you accept?",
        "answer": "We accept USD, CAD, EUR, and GBP. Currency conversion is handled automatically at checkout.",
        "category": "Payment",
        "keywords": ["currency", "international payment", "conversion"]
    },
    {
        "question": "How do I use multiple promo codes?",
        "answer": "Only one promo code can be used per order. Choose the best discount for your purchase.",
        "category": "Payment",
        "keywords": ["multiple codes", "stack coupons", "combine discounts"]
    },
    {
        "question": "How do I track my order?",
        "answer": "You can track your order using the tracking number sent to your email after shipment.",
        "category": "Orders",
        "keywords": ["track", "tracking", "order status"]
    },
    {
        "question": "Can I cancel my order?",
        "answer": "Orders can be cancelled within 2 hours of placement. After that, please contact customer service.",
        "category": "Orders",
        "keywords": ["cancel", "cancellation", "modify"]
    },
    {
        "question": "Can I change my shipping address after placing an order?",
        "answer": "You can change your shipping address within 2 hours of placing an order. After that, please contact customer service immediately.",
        "category": "Orders",
        "keywords": ["address", "shipping address", "change address", "modify order"]
    },
    {
        "question": "Can I exchange an item for a different size/color?",
        "answer": "Yes, you can exchange items within 30 days. Contact customer service to arrange the exchange.",
        "category": "Orders",
        "keywords": ["exchange", "swap", "size", "color", "variation"]
    },
    {
        "question": "What is your order minimum?",
        "answer": "There is no minimum order amount. However, orders under $25 may incur a small processing fee.",
        "category": "Orders",
        "keywords": ["minimum order", "order amount", "processing fee"]
    },
    {
        "question": "How do I create an account?",
        "answer": "Click the 'Sign Up' button on our homepage and follow the registration process. You'll need to provide your email and create a password.",
        "category": "Account",
        "keywords": ["register", "signup", "create account", "new user"]
    },
    {
        "question": "I forgot my password. How can I reset it?",
        "answer": "Click the 'Forgot Password' link on the login page. Enter your email address and we'll send you a password reset link.",
        "category": "Account",
        "keywords": ["password", "reset", "forgot password", "login issue"]
    },
    {
        "question": "How do I leave a product review?",
        "answer": "Sign in to your account, go to 'Order History', find the product, and click 'Write a Review'.",
        "category": "Account",
        "keywords": ["review", "feedback", "rating", "testimonial"]
    },
    {
        "question": "How do I unsubscribe from marketing emails?",
        "answer": "Click the 'Unsubscribe' link at the bottom of any marketing email, or update your preferences in your account settings.",
        "category": "Account",
        "keywords": ["unsubscribe", "emails", "marketing", "newsletter"]
    },
    {
        "question": "How do I check my order history?",
        "answer": "Log into your account and click 'Order History' to view all past and current orders.",
        "category": "Account",
        "keywords": ["order history", "past orders", "account dashboard"]
    },
    {
        "question": "How do I change my account email?",
        "answer": "Go to Account Settings > Personal Information to update your email address. You'll need to verify the new email.",
        "category": "Account",
        "keywords": ["change email", "update email", "account settings"]
    },
    {
        "question": "How do I delete my account?",
        "answer": "To delete your account, contact customer service or use the 'Delete Account' option in Account Settings.",
        "category": "Account",
        "keywords": ["delete account", "close account", "remove data"]
    },
    {
        "question": "What if the item I want is out of stock?",
        "answer": "You can sign up for stock notifications on the product page. We'll email you when the item becomes available.",
        "category": "Products",
        "keywords": ["out of stock", "unavailable", "restock", "notification"]
    },
    {
        "question": "Do you have size guides?",
        "answer": "Yes, each product page includes detailed size guides and measurements to help you choose the right size.",
        "category": "Products",
        "keywords": ["size guide", "measurements", "fit", "sizing"]
    },
    {
        "question": "How do I check product availability?",
        "answer": "Product availability is shown on each product page. You can also call customer service for inventory checks.",
        "category": "Products",
        "keywords": ["availability", "stock", "inventory", "in stock"]
    },
    {
        "question": "Do you offer gift wrapping?",
        "answer": "Yes, we offer gift wrapping for an additional $5 per item. You can select this option at checkout.",
        "category": "Services",
        "keywords": ["gift", "wrapping", "presentation", "gift box"]
    },
    {
        "question": "Do you offer assembly services?",
        "answer": "Yes, we offer assembly services for furniture and large items for an additional fee. Select at checkout.",
        "category": "Services",
        "keywords": ["assembly", "installation", "setup", "service"]
    },
    {
        "question": "Do you offer express checkout?",
        "answer": "Yes, express checkout is available for returning customers. Your payment and shipping information will be auto-filled.",
        "category": "Services",
        "keywords": ["express checkout", "quick checkout", "fast payment"]
    },
    {
        "question": "Do you have a loyalty program?",
        "answer": "Yes! Our loyalty program offers points for every purchase that can be redeemed for discounts.",
        "category": "Programs",
        "keywords": ["loyalty", "rewards", "points"]
    },
    {
        "question": "Do you have affiliate programs?",
        "answer": "Yes, join our affiliate program to earn commissions on referrals. Sign up at affiliates.example.com.",
        "category": "Programs",
        "keywords": ["affiliate", "referral program", "partnership", "commission"]
    },
    {
        "question": "Do you offer bulk discounts?",
        "answer": "Yes, we offer discounts for orders of 10+ items. Contact our sales team for custom pricing on bulk orders.",
        "category": "Pricing",
        "keywords": ["bulk", "wholesale", "volume discount", "large order"]
    },
    {
        "question": "Do you offer student discounts?",
        "answer": "Yes, students get 15% off with valid .edu email address. Verify your student status through our checkout process.",
        "category": "Pricing",
        "keywords": ["student", "education", "discount", "academic"]
    },
    {
        "question": "Do you offer military discounts?",
        "answer": "Yes, active and retired military personnel receive 20% off with valid military ID verification.",
        "category": "Pricing",
        "keywords": ["military discount", "veteran discount", "service member"]
    },
    {
        "question": "What if I receive a damaged item?",
        "answer": "Please contact us immediately with photos of the damaged item, and we'll arrange a replacement.",
        "category": "Issues",
        "keywords": ["damaged", "broken", "defective"]
    },
    {
        "question": "What if my package is lost?",
        "answer": "If your package is lost, contact us immediately. We'll file a claim with the carrier and send a replacement or refund.",
        "category": "Issues",
        "keywords": ["lost package", "missing delivery", "carrier issue"]
    },
    {
        "question": "What security measures do you have?",
        "answer": "We use SSL encryption, secure payment processing, and never store your credit card information on our servers.",
        "category": "Security",
        "keywords": ["security", "encryption", "protection", "fraud prevention"]
    },
    {
        "question": "Do you offer technical support?",
        "answer": "Yes, our technical support team is available Monday-Friday 9 AM-6 PM EST via phone or live chat.",
        "category": "Support",
        "keywords": ["technical support", "help desk", "assistance", "troubleshooting"]
    },
    {
        "question": "How do I report a website issue?",
        "answer": "Report website issues to webmaster@example.com with details about the problem and your browser/device information.",
        "category": "Support",
        "keywords": ["website issue", "bug", "technical problem", "error"]
    }
]
