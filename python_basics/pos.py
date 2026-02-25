<!DOCTYPE html>

<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Supermarket POS</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "primary": "#2bee4b",
                        "background-light": "#f6f8f6",
                        "background-dark": "#102213",
                    },
                    fontFamily: {
                        "display": ["Inter"]
                    },
                    borderRadius: {"DEFAULT": "0.25rem", "lg": "0.5rem", "xl": "0.75rem", "full": "9999px"},
                },
            },
        }
    </script>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="bg-background-light dark:bg-background-dark font-display text-slate-900 dark:text-slate-100">
<div class="relative flex h-screen w-full flex-col overflow-hidden max-w-md mx-auto bg-white dark:bg-background-dark shadow-2xl">
<!-- Header -->
<header class="flex flex-col gap-3 px-4 pt-6 pb-4 border-b border-slate-200 dark:border-slate-800">
<div class="flex items-center justify-between">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-primary text-3xl">shopping_basket</span>
<h1 class="text-xl font-bold tracking-tight">Supermarket POS</h1>
</div>
<button class="flex items-center justify-center size-10 rounded-full bg-slate-100 dark:bg-slate-800">
<span class="material-symbols-outlined text-slate-600 dark:text-slate-400">person</span>
</button>
</div>
<!-- Search Bar -->
<div class="relative">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">search</span>
<input class="w-full pl-10 pr-4 py-3 bg-slate-100 dark:bg-slate-800 border-none rounded-xl focus:ring-2 focus:ring-primary text-sm" placeholder="Search items (Milk, Bread, etc.)" type="text"/>
</div>
<!-- Categories -->
<div class="flex gap-4 overflow-x-auto pb-1 no-scrollbar">
<button class="px-4 py-1.5 rounded-full bg-primary text-slate-900 font-semibold text-xs whitespace-nowrap">All Items</button>
<button class="px-4 py-1.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 font-medium text-xs whitespace-nowrap">Dairy</button>
<button class="px-4 py-1.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 font-medium text-xs whitespace-nowrap">Bakery</button>
<button class="px-4 py-1.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 font-medium text-xs whitespace-nowrap">Produce</button>
<button class="px-4 py-1.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 font-medium text-xs whitespace-nowrap">Pantry</button>
</div>
</header>
<!-- Main Product List -->
<main class="flex-1 overflow-y-auto p-4">
<div class="grid grid-cols-2 gap-4">
<!-- Product Card Template -->
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Fresh white milk in glass bottle" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuBj7pESzMa09e47cBTwNINjCk5ygx0epBa59A8CqnDzgU2XHjhDymWwRNT0pseC2YMVLMS-67bPphF-L45pHb8E5-2Q0UYOUkXHwR3BnU_DWM5GAsigS0BXDq0V-TCGKapHzz4fYn76Ms0y1TLxdNKjlRv9q7fn1eW8eP_JtK7n3r4lrMlYSbnuM89ya-yPu4Pu6V11U3AK5uV2cHL_j2AjEbDdN7cQTNzGEDv7fAxfoVh6DwrVUTN6keswhfXFCorrN1vk8HMRVN4')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Fresh Milk</h3>
<p class="text-primary font-bold text-lg mt-1">$3.50</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Loaf of fresh whole wheat bread" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuD4vf96Vgg5RTW_x6UdY2P_LlMf9uXzav8mgjLvN8A7tS6XJQzj4DhdOxOsl6Lu2uuP2apdMjdB-jeWX3fuTaD-tqaS5XWasZEDOmIUNPRSWfmyb81hk0nrC_vBu2R4k6XverArfkaPnQF4Aut9JfGYop4_1C9V8D24W7IxcJAfvoqEsKdfYh9oAFsM87amgxovMo5eal_Y4HavTQGf1YMGhhIQncWhboFzfw3JxL7DMgUkZzE35HuEW1QV6zQpVFPhSHtZyyiTgl0')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Bread</h3>
<p class="text-primary font-bold text-lg mt-1">$2.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Box of organic brown eggs" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAfOBjMxrSBdZaudZctL5UAcwwKZT1IHG7ZlU4Jt8hYxajlDoIc5UtxSKlijbCKcv2_tJ1YtStZMYoG1ajJcucHqFBhHa_lh4mTmT8cXpVIEoLSfwe5ydoJJqn0-6OqqasfjjwDkC0llDfikc2NwSC_7lpnLDDgzekua5YaNj1cIvq6h7zevwZo9HY_K6ecbJreCxXL_0sicfqhDja8SV7Ng5yvnGYvOJ7G7qWrTrhf8AavEMZCr8CjO2v1Y0Evyb1MFOCOf9NrpeQ')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Eggs (12pk)</h3>
<p class="text-primary font-bold text-lg mt-1">$4.50</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Bag of long grain white rice" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAtZyNvSlc30xRi__1Vwe93S-lPGNmwYL1w0DCd_AQak1EueCU5OZAOPxZH16LJYOuYSa5f3qnlSBCmInJsGJf2H_ImB57ApVLLjphJfRCp9JsMeP5gIb8Ihjqrhdix4rhcgFW-bLFvxaUNxs9Nn_kXjT4bcQJVBoOG5e1so9Dd7Vhde6BbyO0ikXKWHFwqAwnvsrDU-xrAF_rnII7eTysG2aT-1V1cW6NLtAEYvpCunoSanka72yenMa3Sb_s4xy6G6aylUCBAdKw')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">White Rice</h3>
<p class="text-primary font-bold text-lg mt-1">$5.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Red ripe apples in a pile" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAZUvBr9H5o-9EhRdCq7XzHoq6LMVygpNBbI6bYpswEwZQukDxEo-djlo7zsSJV1MoKc7PUq6V0RKJMn47wZJbJIy1pta8iW0pT805k6qg27qahoTHmAn36xTvODxGt3XzYMU7NIDvcnBR5-Z_bpoOA_EC5EAs8h5HA5ybklDxKU4J0ITGgA_3ph0_Lx8SftWOn7rxk2I_wK7lZO6Vaq0pWEfVkKHvFccJO6g7ySOqaR5ewfvUW3Pf2dfXc9qmhmHn6cCoUmg5P-a4')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Apples (1kg)</h3>
<p class="text-primary font-bold text-lg mt-1">$1.50</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Bunch of yellow bananas" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAQqdXB81b9tQ62IfQG0sWQdnNmyYZwx9dfwLEMg2xcALh5yT3LavyIDyGGv21wv3r9nywLvMvtawHRddTo6ObqNWJWYnlQgNQv7E3jLQpFAU19L8BXY4TwqXmHdu8eT7LZWvRzpVFOxH8c1BaSLOqbxyKygNCsw60fGGiZW08cTEKF22CMb9cUjrGogmP5VqKvMPdatne2f5vHPG_y-xihuIoXoUZT3c8468jQ58nWOriF7jU9cBudp6E9AvLV1AH_wEZoRml5Wbk')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Bananas</h3>
<p class="text-primary font-bold text-lg mt-1">$1.20</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Potatoes in a burlap sack" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAfb08_M3x8M7OQU86H8ckNXaZ33e6ayNv_iU_orlOz4_9h_6OGxHU0YgaFoPWsV_Kuv4ZNe1p5McwMGn1Bl0S0Y0suGNKKL4Nr0gyYrkyMJnsSR9Gk_vNq7agkp3s4LBPfKQUVSrHsQfSrkcDZ0cku_La3u5gn_a_69YeGuQMBZxt5h6JMFJKOtwNHYjrzmvxOh3g8NAQCuvw1BQqgpuqDIRPuG0vrnTtfhq7samzTd9DUmAN2X2w3w1yxHIuBy7NkRaYRlq3ctGY')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Potatoes (2kg)</h3>
<p class="text-primary font-bold text-lg mt-1">$3.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Yellow and red onions" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuCa7nZ6LooMRRXR_xlq6eNJDTQP_QEa2odMTNT47N09U4Nh8kP36P-9Jr9Hh53DbaQIcclM_A9-snLi4YBMTwY8RSfTcBTfVee8K6Q7QPSRjE4c-vKjPVgNPqSC1Aiecn3OlYPvLt_XQxm4KK28rFFvhHA0Qa3pyWxixs4eJDIeGnktf9DBq0V8rsNXFLbcdRHoYy9xbvV-SHRnE-k7dCYKb1U1nuKxvFRNvdLm6iA3idYWTZjJFXs3bu2cMh4jzLKNcfGh5mntKAU')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Onions</h3>
<p class="text-primary font-bold text-lg mt-1">$2.50</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Raw chicken breast fillets" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuCYd51ISiPv7lWhyImW9_5jSpb0ApKW55Gn8U2FCexPiFUTSemRTycBMGlqfKRWkccO6mO8iVaQfhlpo_C_Pv7KYActsZTOmlwW7ZzwOucWK94z9m56eLWpcU4FBGuf3GvcFDM_hP5TxMRmEN8B4vHvAfFxpfbKKL59i3GpdTPlMlYIqignQ9OrrcubtZCpf5D2I5fo7gLB_Upj04b7K7LvIWKOIc_37E6yOZWi8_UHgIqC8Q_2EqAy82NZJc2RJeLnpTHzWz6GfBM')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Chicken Breast</h3>
<p class="text-primary font-bold text-lg mt-1">$8.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Dry penne pasta noodles" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuBZeLKycLpH_tXqi8ECwRVYBw3BctJRXLA_J-IF99bFgl6S8tbr4R9A2aV7pWhjMZpqSZlJ5M-yxkIMxB7AuMKwrgn8C6eWV-kI5iWmtGmfnICxHnyfzK9iBomFC-_D7gsIi7Ky69whC5kKTaqN3Oag6ZAtJUlc5A_BnNVunKZ1HfsR3hbjiTd-y636wBVlzcCByrYngDJY33b1_i3IfWO1lYI52b4xyiaFwCtCmgRMO5wak4FyTzfw2j6PMWpsAsBQwSxmMG8_9R8')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Penne Pasta</h3>
<p class="text-primary font-bold text-lg mt-1">$1.80</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Jar of tomato pasta sauce" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuBXH0gvAmkSAvz8N1-6NlCcmcw2cWhjzzz_FWSkd542xT7MOkTGMrAzxTuwEHdaBIROIsrR-pm5OIE1_uXiiBC3yruzxt8eNn9yydIZpjr6A7umWJIZm5QfysB6_hfJOGbidX5oj2QZrgSonrMDG0CHjnd8EVxWXMLDIB4ezyHi1qjUpsAhNF8Lr911BqUlMQIgNYQewk_S3XYbPgtVt8xKIu4KvqEJJlS22PJYVoT5rlxhR89LBTG-Z-VdiOY6th4lYU0MerKRucE')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Tomato Sauce</h3>
<p class="text-primary font-bold text-lg mt-1">$2.20</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Liquid laundry detergent bottle" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAaIcR0aGs0Ll8IMVuVH2Sft9sb3JzEx6TkRZZQBgqkHu1ISt76XH2y4VKd-jeBPC9eADmdtaZQmYIAl2lorWkPvC9c90KgI2BbS51bAeiEjIoW_FSejD_ybkvBc0K_bcMhID1vJv3kzrbRdPJaYo1is-B2wjJpk_vXk2AJwZz3SjOk3nSLZ3DtJ7YEa4Kbn2T1h5QGYk_a1zSdjnWpqmKeyKaqfA22ooGDLpa-OKjZtfzclnRYxbQsgbT3VttZXrMtn0vLaR64hA0')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Detergent</h3>
<p class="text-primary font-bold text-lg mt-1">$12.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Bar of organic herbal soap" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuB1w52uqKmqijapts-BaTCApti2N6MaHnncj6g7OGphJpT5C-BRcTHeu8vAkBkPCf5CniFAF8iKbgKosEvzZwAOZBXuSFzBJ3FJIv5ezzG6-V7iECm70rsvAOML9ZIgR1eknnxSwiI2km1z677nzMA5L4DcomFkILOYh5bRldJDTgnVLs7ffoJt_T0yfnkh_JCYu6cwRIBA0R-dNCA2hNw7GNUmosNDihsyu454QJZZ-ATPR-STGhz1nKcoKZBcOYhlXjCspNiZkow')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Hand Soap</h3>
<p class="text-primary font-bold text-lg mt-1">$1.50</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Plastic bottle of hair shampoo" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAMF8K-UCooxwj96q_Sw0RMl66FID09imPpMhdn0MP_GMqQEqYKIaZyrk4FqdAWN2FcUiN4sU-wAByIEOHd8U8Rwlb2KqfracEzFXw2XZKzHyMw-yClSGviZjGAspBeA59JHOvQRZMEU--537zPFmNBv2b03TdRiVAeDTp-7mKOTYd-_sXvY6aQGzYpo1kRhfycZ-L_K1LBChz0lFbZ7oWHmmyjWyeaeQlstTQ526MHg6R6NpVFGfEBSX30HzSnsDbpD4nf20gQLoI')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Shampoo</h3>
<p class="text-primary font-bold text-lg mt-1">$5.50</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Tube of mint toothpaste" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuCWUfGJi-pfYu1kgguIJAgbI2OKCUL8FVmKKOvxaToqS1lDemsegR9GlSXFCRazJydRny3BMc26U1D_PeoEZr3qQHs2RVb4buS75DgImyXCQ1h8-X8vvfMFsFq-DsEEqEQxiRIy2WepE_gjWpLRxqu0I0WSfe4n1jjgpJRxAVPkqW46fNpldn5WNJCAHshM5EAV3U1MEzanuviEe-7MluMiRtXQOpGjeHQxp5xAHTbq7Q08wG0wtXA-QrhSZpE_Dh1GRem2GUWf6R8')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Toothpaste</h3>
<p class="text-primary font-bold text-lg mt-1">$3.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Bag of roasted coffee beans" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuD0z6r_M8I01nRxd7lnxnQVoBs3a6GHhG7yVwJJlqvxrEo_pIS37Y4O59iM1fl5qnZHFpmr8mwNckHLTzCYQ2eR9SssxfaohgpipBmdWJkFenivQYraAYXJTeWCY6M5BlpaDJvUH1GzAdCYgI2RxUaP1CB62Vl4jKqTiahDH-uKdBYtvC1ywTaor6LKPNI1CrlBFKnbbznWvh7JKLdtlCW16dJukqX7vEDEKa2V3LTp7thMZnpEvaw58QxjXA0AhiW10pWu-rnXnok')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Coffee Beans</h3>
<p class="text-primary font-bold text-lg mt-1">$7.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Assorted tea bags in a box" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuBcFSaE6FNbQr9V1K1CLDT3ebSvbGVeNogh17i06vSqgYZe4JjV7kUOfj4zfWyZNYlWXitRKIfKfMYISweEC6UwkvM7oZ0F3tqy8GR_srKlDJM8JJqOUAFvlCm7-RFSS_vxRXc2XbhiMU7VL0DxD8K2bngGG0rtg3g4B5LqUfkcH03lCt448jCRnMqoyCAsySrZrZuJDZfLjprR2g5u9L3JVOnkBbb3hvGLQbsslnVzlFMh9wyuH1CnWx9TJKeMhdp9fqOqQhFMlxY')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Tea Bags</h3>
<p class="text-primary font-bold text-lg mt-1">$4.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Bag of granulated white sugar" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAgCCsqPsUpBHiQQKVElnLLSuiY80Eo54GHve4Uh_LtgDHCO3ZFWwsO88pWaZnE-ynuWKub_Tzpydv2cjiXzgF8gbpXpjTxgcmHDlpkNUpYPyrYZxvahrPGNJWXou07rMHoVNz1LhQs_HX1T1qS3Fb0aZZNcuOcXmyF68HjWfzK2OJu2XF2lT3P8DiDxk-iNxfzsUx18-3gYGDC34qj96Ze-sDXYZlVhFPJWkg_FL4xTQI6kNHwxnFXF8X6O8YdLn5rp67PTOK7DZs')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Sugar (1kg)</h3>
<p class="text-primary font-bold text-lg mt-1">$2.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Paper bag of all-purpose flour" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuA0zsdQI52FrgH1zWO1jmXZXHnlQIEuq9PK0cuPUPzk6kZVr5byeSvC26IF2BAj7Xtzu8jm6ELJvbQHEzdqtcs-qZX3Pi8eh8CIHulnrjLdh5mLs8KDAh13f1VDJZAvxehFv0qzsCINfiTSeF0gh-HZ83vww_abVyyqy0KO4Q1KXdnWhwlRle0giAv8SGbNQbTUs3Vmog_--LkiDh0gRn8ER_VQpgPlW4H0vju3rxjdcArrsJ4IQMEy9LdxY7ietK7tHY-rzbpZbso')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Flour (1kg)</h3>
<p class="text-primary font-bold text-lg mt-1">$2.50</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
<div class="bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-xl overflow-hidden shadow-sm flex flex-col">
<div class="h-32 bg-slate-200 dark:bg-slate-800 bg-cover bg-center" data-alt="Bottle of golden sunflower oil" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuDzMNn2Kv9pjRL5jdWHs2gvErBXrkOC2Genouv1JKPObSDeZAwkq3NDnl6_7McCNGJrLeCzSMhFwEt6YAzjyaU2Y70jVZ31UelAoTMFEmIPPHPMgHz2KzFNej2bRYlLEUx5RI7Y8WntnK-0Y874cHZPA7YV_8nvrTY9f3BE8JXCVvDg9WxU4pFtvHP0PXYBmGpdctLWLC8eys4LSOUsZRpUzlmBhlfIQ6qs49eP_7eaykIzodTjBboodypI0Edlt17cb65fCAJSOgY')"></div>
<div class="p-3 flex flex-col flex-1">
<h3 class="font-semibold text-sm">Cooking Oil</h3>
<p class="text-primary font-bold text-lg mt-1">$6.00</p>
<button class="mt-3 w-full py-2 bg-primary/10 hover:bg-primary/20 text-slate-900 dark:text-primary font-bold rounded-lg text-xs transition-colors flex items-center justify-center gap-1">
<span class="material-symbols-outlined text-sm">add_shopping_cart</span>
                            Add to Cart
                        </button>
</div>
</div>
</div>
</main>
<!-- Summary Bar & Footer -->
<footer class="bg-white dark:bg-background-dark border-t border-slate-200 dark:border-slate-800 pb-6 pt-4 px-4">
<div class="flex items-center justify-between mb-4">
<div class="flex flex-col">
<span class="text-slate-500 text-xs font-medium uppercase tracking-wider">Total Items</span>
<span class="text-slate-900 dark:text-slate-100 font-bold text-lg">0 Items</span>
</div>
<div class="flex flex-col text-right">
<span class="text-slate-500 text-xs font-medium uppercase tracking-wider">Total Amount</span>
<span class="text-primary font-bold text-2xl">$0.00</span>
</div>
</div>
<button class="w-full bg-primary py-4 rounded-xl text-slate-900 font-bold text-lg shadow-lg shadow-primary/30 flex items-center justify-center gap-2">
                Checkout
                <span class="material-symbols-outlined">arrow_forward</span>
</button>
<!-- Bottom Navigation -->
<div class="flex justify-around mt-6 -mx-4 border-t border-slate-100 dark:border-slate-800 pt-2">
<a class="flex flex-col items-center gap-1 text-slate-900 dark:text-primary" href="#">
<span class="material-symbols-outlined">storefront</span>
<span class="text-[10px] font-bold">Inventory</span>
</a>
<a class="flex flex-col items-center gap-1 text-slate-400" href="#">
<span class="material-symbols-outlined">receipt_long</span>
<span class="text-[10px] font-bold">Orders</span>
</a>
<a class="flex flex-col items-center gap-1 text-slate-400" href="#">
<span class="material-symbols-outlined">monitoring</span>
<span class="text-[10px] font-bold">Analytics</span>
</a>
<a class="flex flex-col items-center gap-1 text-slate-400" href="#">
<span class="material-symbols-outlined">settings</span>
<span class="text-[10px] font-bold">Settings</span>
</a>
</div>
</footer>
</div>
<style>
        /* Hide scrollbar for Chrome, Safari and Opera */
        .no-scrollbar::-webkit-scrollbar {
            display: none;
        }

        /* Hide scrollbar for IE, Edge and Firefox */
        .no-scrollbar {
            -ms-overflow-style: none;  /* IE and Edge */
            scrollbar-width: none;  /* Firefox */
        }
    </style>
</body></html>