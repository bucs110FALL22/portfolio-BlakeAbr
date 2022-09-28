article = "High in dense bamboo forests in the misty, rainy mountains of southwestern China lives one of the world's rarest mammals: the giant panda, also called the panda. Only about 1,500 of these black-and-white bears survive in the wild.  Pandas eat almost nothing but bamboo shoots and leaves. Occasionally they eat other vegetation, fish, or small mammals, but bamboo accounts for 99 percent of their diets. Pandas eat fast, they eat a lot, and they spend about 12 hours a day doing it. The reason: They digest only about a fifth of what they eat. Overall, bamboo is not very nutritious. To stay healthy, they have to eat a lot—up to 15 percent of their body weight in 12 hours—so they eat fast. Pandas' molars are very broad and flat. The shape of the teeth helps the animals crush the bamboo shoots, leaves, and stems that they eat. They can chomp on bamboo up to one-and-a-half inches thick. To get the bamboo to their mouths, they hold the stems with their front paws, which have enlarged wrist bones that act as thumbs for gripping. A panda should have at least two bamboo species where it lives, or it will starve.  A scarcity in bamboo threatens the already limited panda population. An adult female panda weighs 200 pounds. Pandas can climb as high as 13,000 feet and are also very good swimmers. Sometimes male pandas relax by doing handstands against trees. Pandas are shy; they don't venture into areas where people live. This restricts pandas to very limited areas."

substitutions = {
    "panda ":"dog",
    "Pandas":"Dogs",
    "bamboo":"bone",
    "trees":"fire hydrants",
    "eat":"munch"
}


for key, value in substitutions.items():
  article = article.replace(key,value)

print(article)