#!/usr/bin/env python
import sys
from .crew import BdCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'customer_domain': 'mantle.xyz vs base.org',
        'project_description': """
Comprehensive competitor analysis between Mantle Network and Base Chain focusing on onchain revenue performance. This research project will compare two major Ethereum Layer 2 solutions: Mantle (optimistic rollup with innovative data availability) vs Base (Coinbase's optimistic rollup). The analysis will examine transaction volumes, gas fee revenues, total value locked (TVL), daily active users, protocol revenues, ecosystem adoption rates, and revenue growth trajectories. Key focus areas include DeFi ecosystem development, institutional adoption, developer activity, and revenue per user metrics to determine which L2 solution demonstrates superior onchain revenue generation and growth potential.

Customer Domain: Blockchain Infrastructure and Layer 2 Solutions
Project Overview: Head-to-head competitor analysis of Mantle vs Base chain onchain revenue performance, market share, and growth strategies in the competitive L2 ecosystem.
"""
    }
    BdCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'customer_domain': 'mantle.xyz vs base.org',
        'project_description': """
Comprehensive competitor analysis between Mantle Network and Base Chain focusing on onchain revenue performance. This research project will compare two major Ethereum Layer 2 solutions: Mantle (optimistic rollup with innovative data availability) vs Base (Coinbase's optimistic rollup). The analysis will examine transaction volumes, gas fee revenues, total value locked (TVL), daily active users, protocol revenues, ecosystem adoption rates, and revenue growth trajectories. Key focus areas include DeFi ecosystem development, institutional adoption, developer activity, and revenue per user metrics to determine which L2 solution demonstrates superior onchain revenue generation and growth potential.

Customer Domain: Blockchain Infrastructure and Layer 2 Solutions
Project Overview: Head-to-head competitor analysis of Mantle vs Base chain onchain revenue performance, market share, and growth strategies in the competitive L2 ecosystem.
"""
    }
    try:
        BdCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
