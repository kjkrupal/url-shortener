from aws_cdk import core, aws_dynamodb, aws_lambda, aws_apigateway


class UrlShortenerStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Dynamodb
        table = aws_dynamodb.Table(
            self,
            "mapping-table",
            partition_key=aws_dynamodb.Attribute(
                name="id", type=aws_dynamodb.AttributeType.STRING
            ),
        )

        # Lambda function
        function = aws_lambda.Function(
            self,
            "backend",
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            handler="handler.main",
            code=aws_lambda.Code.asset("./lambda"),
        )

        # Grant permissions to our lambda function to read and write to dynamodb table
        table.grant_read_write_data(function)

        # Add dynamodb table name environment variable to be used by our lambda function
        function.add_environment("TABLE_NAME", table.table_name)

        # API to access the lambda function
        api = aws_apigateway.LambdaRestApi(self, "api", handler=function)
