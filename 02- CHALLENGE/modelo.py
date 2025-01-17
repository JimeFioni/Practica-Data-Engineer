from __future__ import annotations
from typing import Any, List, Optional
from pydantic import BaseModel, Extra

class JobPost(BaseModel):
    name: str
    description: str
    key_qualifications: str
    additionals: str
    location: str
    date: str


MX-BusinessPro = JobPost(
    name='MX-Business Pro',
    description='You lead customer engagement, deepen relationships, drive sales and awareness of Apple’s value proposition for business and build loyalty with a focus on high potential business customers. You plan and forecast business performance through account management, pipeline building, and opportunity management, utilizing CRM and other tools. You are passionate and confident and engage business customers by showcasing our technology and helping them discover how Apple and third-party solutions and services can transform the way they work. You develop effective account plans to start and expand adoption of Apple solutions across our ecosystem platform and deeper in the customer’s organization.  You lead and support briefings and leverage workshops to support customer engagement. You effectively use CRMs to build and maintain accurate customer account information, manage relationships, opportunities, tasks, and develop customer insights based on best practices. You mentor and act as a subject matter expert among peers on business customer needs and solutions. You seek, analyze, interpret, and share feedback from Business NPS to continually improve the customer experience. You partner with the Business Development Manager and account team to seamlessly transition accounts in line with account engagement strategy and ensure a smooth customer experience. You maintain process mastery of all Retail Business programs and offerings to ensure compliance with policies and procedures.',
    key_qualifications='At least three years of success and high performance in sales of technology or business solutions, or equivalent.Proven ability to take a personalized, solution-based approach to customer needs.Advanced consultative expertise in Apple and third-party solutions, mobility adoption, and business transformation.Contribute to an inclusive environment through respecting each others’ differences and having the curiosity to learn.Demonstrate Apple’s values of inclusion and diversity in daily activities.',
    additionals='• You have outstanding communication skills, both written and oral, in person and on the phone.• You have the ability to work effectively with business owners and executives across all levels of an organization.• You have excellent organizational and process management skills, ability to set priorities, and  responsiveness to customer requests.• You have the ability to adapt in a dynamic, ever-changing retail environment.',
    location='Apple Retail',
    date='Feb 16, 2024',
),


MX-TechnicalSpecialist = JobPost(
    name='MX-Technical Specialist',
    description='As a Technical Specialist, you help new owners get started and current ones get quick, efficient support — developing strong, positive relationships with Apple. When a customer needs assistance, you quickly assess their situation. Sometimes you take care of customers with advice or a solution on the spot, using your knowledge of current Apple technology to help with iPod, iPhone, and iPad devices. At other times, you refer customers to support team members who get them up and running again. You even provide personal training for new customers, helping them acquire the basic skills they need to get started on photo, video, and music projects. The entire store team benefits from your commitment to providing the best care for customers. By helping Apple maintain strong relationships with customers, you are instrumental to our success.',
    key_qualifications='Ability to assess customers’ support needs when they arrive, then provide solutions or refer them to other team membersFlexibility to regularly rotate through different technical specialties and skill setsAbility to thrive on change as products evolveContribute to an inclusive environment through respecting each others’ differences and having the curiosity to learn.Demonstrate Apple’s values of inclusion and diversity in daily activities.',
    additionals='• You\\'re passionate about Apple and eager to share that passion with others.• You\\'re willing to learn and embrace the guidelines behind Apple\\'s unique style of service.• You have strong people skills-you\\'re approachable, a good listener, and empathetic.• You’ll need to be flexible with your schedule. Your work hours will be based on business needs.',
    location='Apple Retail',
    date='Feb 16, 2024',
),


MX-Genius = JobPost(
    name='MX-Genius',
    description='As a Genius, you provide insightful advice and friendly, hands-on technical support to Apple customers in need. You quickly diagnose product issues on the spot, explaining situations with patience and empathy. After determining whether repairs can be done or a replacement is needed, you offer solutions to quickly get users up and running again. Even if you\\'re juggling more than one customer, you stay conscious of their time demands as well as your own. You fulfill Apple\\'s service commitment with style, speed, and skill. And you earn the trust of customers and coworkers alike as you offer guidance, knowledge, and even tips and training.',
    key_qualifications='Strong people skills and a knack for problem solving.Ability to maintain composure and customer focus while troubleshooting and solving technical issues.Ability to adhere to a schedule of customer appointments.Contribute to an inclusive environment through respecting each others’ differences and having the curiosity to learn.Demonstrate Apple’s values of inclusion and diversity in daily activities.',
    additionals='• You have an aptitude for acquiring skills in technical repairs and an eagerness to learn.• You have excellent time management skills and can make decisions quickly.• You’ll need to be flexible with your schedule. Your work hours will be based on business needs.',
    location='Apple Retail',
    date='Feb 16, 2024',
),

MX-OperationsExpert = JobPost(
    name='MX-Operations Expert',
    description='As an Operations Expert, you and your team have the incredible responsibility of ensuring products take the final step in the supply chain: getting into customers\\' hands. You\\'re in charge of the store\\'s entire inventory - products, parts, tools, supplies, and everything else. You make sure your team has the support, knowledge, and resources required to maintain product availability, complete inventory tasks, and keep the stockroom organized as new products arrive. You\\'re in constant contact with the management and leadership teams, sharing data about the status of products and parts. And when exciting new products arrive, you\\'re the first to open them up and present them to the entire store team. Apple makes the products, but you make it happen by being ready to place our products in customers\\' hands.',
    key_qualifications='Ability to think quickly and perform problem-solving tasks, even within changing conditions.Leadership skills, whether guiding by example or coaching a group.Strong organizational skills, quickly evaluating every situation.Contribute to an inclusive environment through respecting each others’ differences and having the curiosity to learn.Demonstrate Apple’s values of inclusion and diversity in daily activities.',
    additionals='• You can manage and meet multiple inventory deadlines each week.• You’re willing to observe guidelines to allow secure access to products and movement through the stockroom.• You’ll need to be flexible with your schedule. Your work hours will be based on business needs.',
    location='Apple Retail',
    date='Feb 16, 2024',
),


MX-Creative = JobPost(
    name='MX-Creative',
    description='As a Creative, your main role at the Apple Store is that of instructor, whether guiding small groups to learn or helping individuals. You use your presentation skills to act as a facilitator, helping users get set up, get trained, and get going. But you\\'re also an excellent listener, taking the time to understand what each user hopes to achieve or learn. By adjusting your teaching style to each user\\'s individual skill level, you maximize their understanding and your own time. You recognize that purchasing a new product can sometimes help customers attain their goals. You spend much of your time leading scheduled sessions, but you\\'re still comfortable interacting with store customers between those sessions. You\\'re proud to enrich the lives of others  - whether customers or team members  - through teaching, in the way only a Creative can.',
    key_qualifications='Passion for education and ability to instruct by letting users learn by doing.Ability to teach small groups and multiple customers simultaneously.Tenacity to work with users to help them get the most out of their devices.Contribute to an inclusive environment through respecting each others’ differences and having the curiosity to learn.Demonstrate Apple’s values of inclusion and diversity in daily activities.',
    additionals='• You’re comfortable selling as well as teaching, helping your team members out as needed.• You’re self-motivated and self-directed, and can adhere to a tightly structured training schedule.• You can be adept at recommending other in-store support options, such as business services and the Genius Bar.• You’ll need to be flexible with your schedule. Your work hours will be based on business needs.',
    location='Apple Retail',
    date='Feb 16, 2024',
),
