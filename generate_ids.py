import uuid

# Your original data
data = [
    {
        "_id": "gtfrftgthyjukilolkio98ko",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-pro-129-2021-1.jpg",
        "name": "iPad Pro 12.9",
        "brand": "Apple",
        "brandImg": "https://i.ibb.co/6WnNwRn/apple.jpg",
        "type": "Tablet",
        "price": 1099,
        "rating": 4.8,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "rhyhjutgfredswedfrtgf454",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-air4-2020-01.jpg",
        "name": "iPad Air 4",
        "brand": "Apple",
        "brandImg": "https://i.ibb.co/6WnNwRn/apple.jpg",
        "type": "Tablet",
        "price": 649,
        "rating": 4.6,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "uyjiiknhvfredsw1234678es",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-mini-2021-2.jpg",
        "name": "iPad Mini 6",
        "brand": "Apple",
        "brandImg": "https://i.ibb.co/6WnNwRn/apple.jpg",
        "type": "Tablet",
        "price": 499,
        "rating": 4.4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "j1k2l3",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-102-2021-1.jpg",
        "name": "iPad 9th Gen",
        "brand": "Apple",
        "brandImg": "https://i.ibb.co/6WnNwRn/apple.jpg",
        "type": "Tablet",
        "price": 329,
        "rating": 4.2,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "m4n5o6",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s7-plus-01.jpg",
        "name": "iPad Pro 11",
        "brand": "Apple",
        "brandImg": "https://i.ibb.co/6WnNwRn/apple.jpg",
        "type": "Tablet",
        "price": 799,
        "rating": 4.7,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "s1a2m3s4u5n6g",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-a7-lite-1.jpg",
        "name": "Galaxy Tab S7+",
        "brand": "Samsung",
        "brandImg": "https://i.ibb.co/nPNFYKv/samsung.jpg",
        "type": "Tablet",
        "price": 849,
        "rating": 4.6,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "g2a3l4a5x6y7t8a9b0",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-active3-1.jpg",
        "name": "Galaxy Tab A7",
        "brand": "Samsung",
        "brandImg": "https://i.ibb.co/nPNFYKv/samsung.jpg",
        "type": "Tablet",
        "price": 229,
        "rating": 4.2,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "s3u4r5f6a7c8e9",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s5e-sm-t725-2.jpg",
        "name": "Galaxy Tab S6 Lite",
        "brand": "Samsung",
        "brandImg": "https://i.ibb.co/nPNFYKv/samsung.jpg",
        "type": "Tablet",
        "price": 349,
        "rating": 4.4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "s4a5m6t7a8b9",
        "image": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenpad-3s-2.jpg",
        "name": "Galaxy Tab Active3",
        "brand": "Samsung",
        "brandImg": "https://i.ibb.co/nPNFYKv/samsung.jpg",
        "type": "Tablet",
        "price": 499,
        "rating": 4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "s5a6m7s8u9n0g",
        "image": "https://images.anandtech.com/doci/5586/ASUS%20Transformer%20Pad_Infinity_02.jpg",
        "name": "Galaxy Tab S5e",
        "brand": "Samsung",
        "brandImg": "https://i.ibb.co/nPNFYKv/samsung.jpg",
        "type": "Tablet",
        "price": 399,
        "rating": 4.5,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a1s2u3s4",
        "image": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenpad-s-80-z580c.jpg",
        "name": "Asus ZenPad 3S 10",
        "brand": "Asus",
        "hp": "https://i.ibb.co/wC0NBbT/asus.webp",
        "type": "Tablet",
        "price": 299,
        "rating": 4.3,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a2s3u4s5",
        "image": "https://ssl-product-images.www8-hp.com/digmedialib/prodimg/lowres/c05521095.png",
        "name": "Asus Transformer Pad Infinity",
        "brand": "Asus",
        "brandImg": "https://i.ibb.co/wC0NBbT/asus.webp",
        "type": "Tablet",
        "price": 449,
        "rating": 4.1,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a3s4u5s6",
        "image": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenpad-3s-2.jpg",
        "name": "Asus ZenPad S 8.0",
        "brand": "Asus",
        "brandImg": "https://i.ibb.co/wC0NBbT/asus.webp",
        "type": "Tablet",
        "price": 199,
        "rating": 4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a4s5u6s7",
        "image": "https://www.hp.com/ch-de/shop/Html/Merch/Images/c07040264_1750x1285.jpg",
        "name": "Asus Chromebook Tablet CT100PA",
        "brand": "Asus",
        "brandImg": "https://i.ibb.co/wC0NBbT/asus.webp",
        "type": "Tablet",
        "price": 299,
        "rating": 4.2,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a5s6u7s8",
        "image": "https://www.hp.com/ch-de/shop/Html/Merch/Images/c08249103_1750x1285.jpg",
        "name": "Asus ZenPad 10",
        "brand": "Asus",
        "brandImg": "https://i.ibb.co/wC0NBbT/asus.webp",
        "type": "Tablet",
        "price": 279,
        "rating": 4.4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "h1p2t3a4b5",
        "image": "https://adminapi.applegadgetsbd.com/storage/media/large/HP-Envy-x360-15-FE0053DX-Core-i7-1335U-13th-Genaration-Intel-Iris-Xe-Graphics-15.6--Touch-Screen-FHD-Laptop-(1)-8960.jpg",
        "name": "HP Spectre x2",
        "brand": "HP",
        "brandImg": "https://i.ibb.co/9bmV8sy/hp.jpg",
        "type": "2-in-1 Laptop/Tablet",
        "price": 1099,
        "rating": 4.5,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "h2p3t4a5b6",
        "image": "https://www.zdnet.com/a/img/2016/01/18/3910ca64-9dc7-4d6f-85d5-da7f4c8c4a46/hp-pro-tab-608-main.jpg",
        "name": "HP Elite x2",
        "brand": "HP",
        "brandImg": "https://i.ibb.co/9bmV8sy/hp.jpg",
        "type": "2-in-1 Laptop/Tablet",
        "price": 899,
        "rating": 4.4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "h3p4t5a6b7",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-pro-129-2021-1.jpg",
        "name": "HP Pavilion x360",
        "brand": "HP",
        "brandImg": "https://i.ibb.co/9bmV8sy/hp.jpg",
        "type": "Convertible Laptop",
        "price": 699,
        "rating": 4.2,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "h4p5t6a7b8",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-air4-2020-01.jpg",
        "name": "HP Envy x360",
        "brand": "HP",
        "brandImg": "https://i.ibb.co/9bmV8sy/hp.jpg",
        "type": "Convertible Laptop",
        "price": 849,
        "rating": 4.3,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "h5p6t7a8b9",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-mini-2021-2.jpg",
        "name": "HP Pro Tablet 608 G1",
        "brand": "HP",
        "brandImg": "https://i.ibb.co/9bmV8sy/hp.jpg",
        "type": "Business Tablet",
        "price": 499,
        "rating": 4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "o1p2h3o4n5e6_t1p2r3o4",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-102-2021-1.jpg",
        "name": "Oppo Find X5 Pro",
        "brand": "Oppo",
        "brandImg": "https://i.ibb.co/Y7PW2hd/oppo.jpg",
        "type": "Smartphone",
        "price": 1099,
        "rating": 4.7,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "o2p3o4_t2a3b4l5e6t",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-pro-11-2022-1.jpg",
        "name": "Oppo Watch 2",
        "brand": "Oppo",
        "brandImg": "https://i.ibb.co/Y7PW2hd/oppo.jpg",
        "type": "Smartwatch",
        "price": 299,
        "rating": 4.5,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "o3p4p5o6_t3a4b5l6e7t",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s7-plus-01.jpg",
        "name": "Oppo Pad Pro",
        "brand": "Oppo",
        "brandImg": "https://i.ibb.co/Y7PW2hd/oppo.jpg",
        "type": "Tablet",
        "price": 799,
        "rating": 4.5,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "o4p5o6_t4a5b6l7e8t",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-a7-lite-1.jpg",
        "name": "Oppo Enco X",
        "brand": "Oppo",
        "brandImg": "https://i.ibb.co/Y7PW2hd/oppo.jpg",
        "type": "True Wireless Earbuds",
        "price": 179,
        "rating": 4.3,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "o5p6o7o8_t5a6b7l8e9t",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-active3-1.jpg",
        "name": "Oppo Reno 6 Z",
        "brand": "Oppo",
        "brandImg": "https://i.ibb.co/Y7PW2hd/oppo.jpg",
        "type": "Smartphone",
        "price": 499,
        "rating": 4.2,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a1c2e3r4_l1a2p3t4o5p6",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s5e-sm-t725-2.jpg",
        "name": "Acer Predator Helios 500",
        "brand": "Acer",
        "brandImg": "https://i.ibb.co/s1bTcfV/acer.jpg",
        "type": "Gaming Laptop",
        "price": 1899,
        "rating": 4.6,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a2c3e4r5_l2a3p4t5o6p7",
        "image": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenpad-3s-2.jpg",
        "name": "Acer Swift 5",
        "brand": "Acer",
        "brandImg": "https://i.ibb.co/s1bTcfV/acer.jpg",
        "type": "Ultrabook",
        "price": 999,
        "rating": 4.4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a3c4e5r6_l3a4p5t6o7p8",
        "image": "https://images.anandtech.com/doci/5586/ASUS%20Transformer%20Pad_Infinity_02.jpg",
        "name": "Acer Predator X34",
        "brand": "Acer",
        "brandImg": "https://i.ibb.co/s1bTcfV/acer.jpg",
        "type": "Gaming Monitor",
        "price": 799,
        "rating": 4.7,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a4c5e6r7_l4a5p6t7o8p9",
        "image": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenpad-s-80-z580c.jpg",
        "name": "Acer Aspire 5",
        "brand": "Acer",
        "brandImg": "https://i.ibb.co/s1bTcfV/acer.jpg",
        "type": "Laptop",
        "price": 549,
        "rating": 4.2,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "a5c6e7r8_l5a6p7t8o9p0",
        "image": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenpad-3s-2.jpg",
        "name": "Acer Predator Orion 9000",
        "brand": "Acer",
        "brandImg": "https://i.ibb.co/s1bTcfV/acer.jpg",
        "type": "Gaming Desktop",
        "price": 2499,
        "rating": 4.8,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "s1o2n3y4_x1p2e3r4_i1a2",
        "image": "https://ssl-product-images.www8-hp.com/digmedialib/prodimg/lowres/c05521095.png",
        "name": "Sony Xperia 1 III",
        "brand": "Sony",
        "brandImg": "https://i.ibb.co/pd3Wg41/sony.jpg",
        "type": "Smartphone",
        "price": 1299,
        "rating": 4.7,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "s2o3n4y5_a17l1p2h3a4",
        "image": "https://www.hp.com/ch-de/shop/Html/Merch/Images/c07040264_1750x1285.jpg",
        "name": "Sony Alpha 7 IV",
        "brand": "Sony",
        "brandImg": "https://i.ibb.co/pd3Wg41/sony.jpg",
        "type": "Mirrorless Camera",
        "price": 2499,
        "rating": 4.8,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "s3o4n5y6_w1h2-1a3a4",
        "image": "https://www.hp.com/ch-de/shop/Html/Merch/Images/c08249103_1750x1285.jpg",
        "name": "Sony WH-1000XM4",
        "brand": "Sony",
        "brandImg": "https://i.ibb.co/pd3Wg41/sony.jpg",
        "type": "Wireless Headphones",
        "price": 349,
        "rating": 4.6,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "s4o5n6y7_b1r2a3v4i1a2",
        "image": "https://adminapi.applegadgetsbd.com/storage/media/large/HP-Envy-x360-15-FE0053DX-Core-i7-1335U-13th-Genaration-Intel-Iris-Xe-Graphics-15.6--Touch-Screen-FHD-Laptop-(1)-8960.jpg",
        "name": "Sony BRAVIA XR A90J",
        "brand": "Sony",
        "brandImg": "https://i.ibb.co/pd3Wg41/sony.jpg",
        "type": "Smart TV",
        "price": 2799,
        "rating": 4.9,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "s5o6n7y8_p1s2_5",
        "image": "https://www.zdnet.com/a/img/2016/01/18/3910ca64-9dc7-4d6f-85d5-da7f4c8c4a46/hp-pro-tab-608-main.jpg",
        "name": "Sony PlayStation 5",
        "brand": "Sony",
        "brandImg": "https://i.ibb.co/pd3Wg41/sony.jpg",
        "type": "Gaming Console",
        "price": 499,
        "rating": 4.7,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "x1i2a3o4m5i6_m1i2_1",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-pro-129-2021-1.jpg",
        "name": "Xiaomi Mi 11 Ultra",
        "brand": "Xiaomi",
        "brandImg": "https://i.ibb.co/X5CJth2/Xiaomi.jpg",
        "type": "Smartphone",
        "price": 1099,
        "rating": 4.8,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "x2i3a4o5m6_m2i3_2",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-air4-2020-01.jpg",
        "name": "Xiaomi Mi Watch Revolve",
        "brand": "Xiaomi",
        "brandImg": "https://i.ibb.co/X5CJth2/Xiaomi.jpg",
        "type": "Smartwatch",
        "price": 129,
        "rating": 4.5,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "x3i4a5o6m7_m3i4_3",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-mini-2021-2.jpg",
        "name": "Xiaomi Mi TV 4S",
        "brand": "Xiaomi",
        "brandImg": "https://i.ibb.co/X5CJth2/Xiaomi.jpg",
        "type": "Smart TV",
        "price": 599,
        "rating": 4.6,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "x4i5a6o7m8_m4i5_4",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-102-2021-1.jpg",
        "name": "Xiaomi Redmi Note 10 Pro",
        "brand": "Xiaomi",
        "brandImg": "https://i.ibb.co/X5CJth2/Xiaomi.jpg",
        "type": "Smartphone",
        "price": 279,
        "rating": 4.4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "x5i6a7o8m9_m5i6_5",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-pro-11-2022-1.jpg",
        "name": "Xiaomi Mi Band 6",
        "brand": "Xiaomi",
        "brandImg": "https://i.ibb.co/X5CJth2/Xiaomi.jpg",
        "type": "Fitness Tracker",
        "price": 49,
        "rating": 4.3,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "d1e2l3l4_i1n2s3p4i5r6o7n8",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s7-plus-01.jpg",
        "name": "Dell XPS 13",
        "brand": "Dell",
        "brandImg": "https://i.ibb.co/NN25ryM/dell.jpg",
        "type": "Laptop",
        "price": 1299,
        "rating": 4.8,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "d2e3l4l5_i2n3s4p5i6r7o8n9",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-a7-lite-1.jpg",
        "name": "Dell Alienware Aurora R12",
        "brand": "Dell",
        "brandImg": "https://i.ibb.co/NN25ryM/dell.jpg",
        "type": "Gaming Desktop",
        "price": 1799,
        "rating": 4.7,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "d3e4l5l6_i3n4s5p6i7r8o9n0",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-active3-1.jpg",
        "name": "Dell Inspiron 14 2-in-1",
        "brand": "Dell",
        "brandImg": "https://i.ibb.co/NN25ryM/dell.jpg",
        "type": "2-in-1 Laptop",
        "price": 799,
        "rating": 4.5,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "d4e5l6l7_i4n5s6p7i8r9o0n1",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s5e-sm-t725-2.jpg",
        "name": "Dell Ultrasharp U2720Q",
        "brand": "Dell",
        "brandImg": "https://i.ibb.co/NN25ryM/dell.jpg",
        "type": "Monitor",
        "price": 599,
        "rating": 4.6,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "d5e6l7l8_i5n6s7p8i9r0o1n2",
        "image": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenpad-3s-2.jpg",
        "name": "Dell G5 15 SE",
        "brand": "Dell",
        "brandImg": "https://i.ibb.co/NN25ryM/dell.jpg",
        "type": "Gaming Laptop",
        "price": 1199,
        "rating": 4.4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l1e2n3o4v5o6_i1d2_e3a4_p5a6d7",
        "image": "https://images.anandtech.com/doci/5586/ASUS%20Transformer%20Pad_Infinity_02.jpg",
        "name": "Lenovo ThinkPad X1 Carbon",
        "brand": "Lenovo",
        "brandImg": "https://i.ibb.co/CM1Rwyr/lenovo.jpg",
        "type": "Laptop",
        "price": 1499,
        "rating": 4.7,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l2e3n4o5v6_o1e2l3i4t5e6_t1a2b3l4e5t",
        "image": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenpad-s-80-z580c.jpg",
        "name": "Lenovo Yoga Tab 13",
        "brand": "Lenovo",
        "brandImg": "https://i.ibb.co/CM1Rwyr/lenovo.jpg",
        "type": "Tablet",
        "price": 599,
        "rating": 4.5,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l3e4n5o6v7_o2e3l4i5t6e7_t2a3b4l5e6t",
        "image": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenpad-3s-2.jpg",
        "name": "Lenovo Smartwatch Elegance",
        "brand": "Lenovo",
        "brandImg": "https://i.ibb.co/CM1Rwyr/lenovo.jpg",
        "type": "Smartwatch",
        "price": 199,
        "rating": 4.2,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l4e5n6o7v8_o3e4l5i6t7e8_t3h4i5n6k7c8e9n0t",
        "image": "https://ssl-product-images.www8-hp.com/digmedialib/prodimg/lowres/c05521095.png",
        "name": "Lenovo ThinkCentre M90n Nano",
        "brand": "Lenovo",
        "brandImg": "https://i.ibb.co/CM1Rwyr/lenovo.jpg",
        "type": "Desktop",
        "price": 799,
        "rating": 4.6,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l5e6n7o8v9_i4d5_e6a7_p8a9d0",
        "image": "https://www.hp.com/ch-de/shop/Html/Merch/Images/c07040264_1750x1285.jpg",
        "name": "Lenovo Ideapad Flex 5",
        "brand": "Lenovo",
        "brandImg": "https://i.ibb.co/CM1Rwyr/lenovo.jpg",
        "type": "Laptop",
        "price": 699,
        "rating": 4.4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l1o2g3i4t5e6c7h_m1o2u3s4e5",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-pro-11-2022-1.jpg",
        "name": "Logitech MX Master 3",
        "brand": "Logitech",
        "brandImg": "https://i.ibb.co/r4QDJbw/Logitech.jpg",
        "type": "Mouse",
        "price": 99.99,
        "rating": 4.7,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l2o3g4i5t6e7c8h_k1e2y3b4o5a6r7d8",
        "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s5e-sm-t725-2.jpg",
        "name": "Logitech K380",
        "brand": "Logitech",
        "brandImg": "https://i.ibb.co/r4QDJbw/Logitech.jpg",
        "type": "Keyboard",
        "price": 49.99,
        "rating": 4.5,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l3o4g5i6t7e8c9h_w1e2b3c4a5m6",
        "image": "https://images.anandtech.com/doci/5586/ASUS%20Transformer%20Pad_Infinity_02.jpg",
        "name": "Logitech C920 Pro HD Webcam",
        "brand": "Logitech",
        "brandImg": "https://i.ibb.co/r4QDJbw/Logitech.jpg",
        "type": "Webcam",
        "price": 79.99,
        "rating": 4.6,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l4o5g6i7t8e9c0h_s1p2e3a4k5e6r7s8",
        "image": "https://ssl-product-images.www8-hp.com/digmedialib/prodimg/lowres/c05521095.png",
        "name": "Logitech G560 LIGHTSYNC Gaming Speakers",
        "brand": "Logitech",
        "brandImg": "https://i.ibb.co/r4QDJbw/Logitech.jpg",
        "type": "Speakers",
        "price": 199.99,
        "rating": 4.8,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "l5o6g7i8t9e0c1h_p1r2o3_g1",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-air4-2020-01.jpg",
        "name": "Logitech G Pro X Gaming Headset",
        "brand": "Logitech",
        "brandImg": "https://i.ibb.co/r4QDJbw/Logitech.jpg",
        "type": "Gaming Headset",
        "price": 129.99,
        "rating": 4.4,
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "658a8c9a07dd7cbd603da3c4",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-1.jpg",
        "name": "iPhone 15",
        "brand": "Apple",
        "type": "Smart Phone",
        "price": "725",
        "rating": "5",
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "658a91f707dd7cbd603da3c5",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-1.jpg",
        "name": "Samsung j7 Pro",
        "brand": "Samsung",
        "type": "Smart Phone",
        "price": "725",
        "rating": "5",
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    },
    {
        "_id": "658ab88607dd7cbd603da3c8",
        "image": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-1.jpg",
        "name": "iPhone 14",
        "brand": "Apple",
        "type": "Smart Phone",
        "price": "725",
        "rating": "5",
        "details": "The iPhone 15 boasts cutting-edge technology and design, featuring a stunning 6.7-inch Super Retina XDR display with ProMotion technology for a seamless and responsive user experience. Powered by the latest A16 Bionic chip, it delivers exceptional performance and efficiency. The device excels in photography with a triple-lens camera system, including a 108MP main sensor, ultra-wide, and telephoto lenses, offering unparalleled image quality and advanced computational photography capabilities. The iPhone 15 supports 5G connectivity, ensuring faster download and streaming speeds. Its sleek design incorporates durable materials, and the device introduces innovative features like enhanced Face ID and extended battery life, making it a flagship device that redefines the smartphone experience."
    }
]

# Function to generate a unique 24-character identifier
def generate_unique_id():
    return str(uuid.uuid4().hex)[:24]

# Update _id for each object in the data
for item in data:
    item["_id"] = generate_unique_id()

# Print the updated data
print(data)
