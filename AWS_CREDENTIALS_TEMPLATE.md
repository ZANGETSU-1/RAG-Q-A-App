# AWS Credentials for Assessment

## 🔑 AWS Access Information

**Table Name**: `assessment-users`
**Region**: `eu-west-1`

**AWS Credentials**:

- **Access Key ID**: `AKIARPWOJWTLWHSCG2FH`
- **Secret Access Key**: `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`

## 🚀 Quick Setup

### For Node.js:

```bash
# Set environment variables
export AWS_ACCESS_KEY_ID="AKIARPWOJWTLWHSCG2FH"
export AWS_SECRET_ACCESS_KEY="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"
export AWS_REGION="eu-west-1"

# Install dependencies
npm install

# Test connection (optional)
node -e "
const { DynamoDBClient, DescribeTableCommand } = require('@aws-sdk/client-dynamodb');
const client = new DynamoDBClient({ region: 'eu-west-1' });
client.send(new DescribeTableCommand({ TableName: 'assessment-users' }))
  .then(data => console.log('✅ Connected to DynamoDB:', data.Table.TableName))
  .catch(err => console.error('❌ Connection failed:', err.message));
"
```

### For Python:

```bash
# Set environment variables
export AWS_ACCESS_KEY_ID="AKIARPWOJWTLWHSCG2FH"
export AWS_SECRET_ACCESS_KEY="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"
export AWS_REGION="eu-west-1"

# Install dependencies
pip install boto3

# Test connection (optional)
python -c "
import boto3
dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
table = dynamodb.Table('assessment-users')
print('✅ Connected to DynamoDB:', table.name)
"
```

## 🗄️ Table Schema

**Table**: `assessment-users`

- **Partition Key**: `PK` (String)
- **Sort Key**: `SK` (String)
- **Attributes**: You can add any attributes you need (name, email, age, etc.)
- **Billing**: On-demand (no need to worry about capacity)

## 🔒 Security Notes

- These credentials have **minimal permissions** - only DynamoDB access to the assessment table
- Credentials are **temporary** and will be deactivated after the assessment
- **Do not share** these credentials with anyone
- **Do not commit** these credentials to your git repository

## 🆘 Troubleshooting

### Common Issues:

**"Unable to locate credentials"**:

```bash
# Make sure environment variables are set
echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY
```

**"ResourceNotFoundException"**:

- Check that you're using the correct table name: `assessment-users`
- Verify you're connecting to the correct region: `eu-west-1`

**"AccessDeniedException"**:

- These credentials only have access to DynamoDB operations
- You cannot access other AWS services with these credentials

## 📞 Support

If you encounter any AWS-related issues:

1. **Check the troubleshooting section above**
2. **Create an issue in this repository** with the error message
3. **Contact the assessment team** if the issue persists

---

**Good luck with Task A!** 🚀
