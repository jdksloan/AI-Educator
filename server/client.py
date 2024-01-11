from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/category_chain/")
print(remote_chain.invoke({"request": "I would like to assess my English language level please"}))
# print(remote_chain.invoke({"request": "1. Hello, my name is Tom. Nice to meet you."
#                                       "2. CrossFit is my favorite hobby because it offers a dynamic and challenging "
#                                       "workout that keeps me engaged and motivated. The variety of exercises and "
#                                       "constantly varied movements keep my workouts interesting and prevent "
#                                       "boredom. Additionally, the supportive and community-oriented atmosphere of "
#                                       "CrossFit gyms creates a sense of camaraderie and encouragement, making it more "
#                                       "than just a workout but also a social experience. The physical and mental "
#                                       "benefits of CrossFit, including improved strength, endurance, and overall "
#                                       "fitness, make it a fulfilling and rewarding hobby that I look forward to "
#                                       "each day. "
#                                       "3. There is most commonly used to mean at that point or in that place. Their "
#                                       "is the possessive form of the third-person plural pronoun they. It means "
#                                       "belonging to them. They're is a shortened version of they are. "
#                                       "4. A blessing in disguise. A dime a dozen. Beat around the bush. Better late "
#                                       "than never. Easy does it. Cutting corners. Break a leg. Hit the sack."
#                                       "5. I recently enjoyed a wonderful holiday in the beautiful countryside. The "
#                                       "serene surroundings and fresh air provided the perfect escape from the hustle "
#                                       "and bustle of everyday life. Exploring the picturesque landscapes, "
#                                       "indulging in delicious local cuisine, and spending quality time with loved "
#                                       "ones made this holiday truly memorable. Whether it was hiking through the lush "
#                                       "forests or simply relaxing by the tranquil lake, every moment was filled with "
#                                       "joy and rejuvenation. This holiday was a much-needed opportunity to recharge "
#                                       "and create lasting memories."}))
