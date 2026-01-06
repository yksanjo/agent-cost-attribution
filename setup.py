from setuptools import setup, find_packages

setup(
    name="agent-cost-attribution",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "anthropic>=0.5.0",
        "openai>=1.0.0",
        "flask>=2.3.0",
        "pandas>=1.3.0",
        "plotly>=5.15.0"
    ],
    author="AI Engineer Community",
    description="SDK for tracking and attributing AI agent costs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/agent-cost-attribution",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)